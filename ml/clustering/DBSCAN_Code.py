import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Step 1: Load the dataset
def load_data(file_path):
    """Load the Mall Customers dataset."""
    data = pd.read_csv(file_path)
    return data

# Step 2: Preprocess the data
def preprocess_data(data):
    """
    Select relevant features for clustering (e.g., Income and Spending Score),
    and scale them.
    """
    features = data[['Annual Income (k$)', 'Spending Score (1-100)']]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features

# Step 3: Apply DBSCAN
def apply_dbscan(data, eps=0.5, min_samples=5):
    """
    Apply DBSCAN clustering algorithm to the preprocessed data.
    """
    db = DBSCAN(eps=eps, min_samples=min_samples)
    db.fit(data)
    labels = db.labels_
    return labels

# Step 4: Plot Results
def plot_clusters(data, labels):
    """
    Visualize the clusters formed by DBSCAN.
    """
    unique_labels = set(labels)
    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]

    for k, col in zip(unique_labels, colors):
        if k == -1:
            col = [0, 0, 0, 1]  # Black for noise

        class_member_mask = (labels == k)
        xy = data[class_member_mask]

        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=6)

    plt.title('DBSCAN Clustering Results')
    plt.xlabel('Annual Income (scaled)')
    plt.ylabel('Spending Score (scaled)')
    plt.show()

# Main function
if __name__ == "__main__":
    # Path to your dataset
    file_path = "Mall_customers.csv"

    # Load and preprocess data
    raw_data = load_data(file_path)
    processed_data = preprocess_data(raw_data)

    # Apply DBSCAN
    labels = apply_dbscan(processed_data, eps=0.3, min_samples=5)
    

    # Number of clusters (excluding noise if present)
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    print(f'Estimated number of clusters: {n_clusters_}')
    # Plot clusters
    plot_clusters(processed_data, labels)
