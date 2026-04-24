from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt

# Sample data
X = np.array([
    [1,2], [2,3], [3,4],
    [10,11], [11,12], [12,13],
    [50,50]  # noise
])
# Create model
dbscan = DBSCAN(eps=2, min_samples=2)

# Train
dbscan.fit(X)

# Output
print("Cluster labels:", dbscan.labels_)
# Output Interpretation
# [0, 0, 0, 1, 1, 1, -1]
# 0, 1 → clusters
# -1 → noise (outlier)
labels = dbscan.labels_
plt.scatter(X[:,0], X[:,1], c=labels, cmap='plasma')
plt.show()