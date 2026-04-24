from sklearn.cluster import KMeans
import numpy as np

# Sample data
X = np.array([
    [1,2], [2,3], [3,4],
    [10,11], [11,12], [12,13]
])

# Create model
kmeans = KMeans(n_clusters=2)

# Train
kmeans.fit(X)

# Output
print("Cluster labels:", kmeans.labels_)
print("Centroids:", kmeans.cluster_centers_)
