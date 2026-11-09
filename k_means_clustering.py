# K-Means Clustering using Iris Dataset

# Step 1: Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Step 2: Load the Iris dataset
iris = load_iris()

# Step 3: Extract input feature data
X = iris.data

# Step 4: Display number of samples and features
print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])

# Step 5: Display feature names
print("\nFeature names:")
for feature in iris.feature_names:
    print(feature)

# Step 6: Create K-Means model with K = 3
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Step 7: Train the K-Means model
kmeans.fit(X)

# Step 8: Obtain cluster labels
labels = kmeans.labels_

# Step 9: Display cluster assignment of each sample
print("\nCluster assignment of each sample:")
for i, label in enumerate(labels):
    print("Sample", i + 1, "-> Cluster", label)

# Step 10: Obtain and display cluster centers
centers = kmeans.cluster_centers_

print("\nCluster Centroids:")
for i, center in enumerate(centers):
    print("Cluster", i, ":", center)

# Step 11: Count samples in each cluster
print("\nNumber of samples in each cluster:")

for i in range(3):
    count = np.sum(labels == i)
    print("Cluster", i, ":", count, "samples")

# Step 12: Calculate and display inertia
print("\nK-Means Inertia:", kmeans.inertia_)

# Steps 13-15: Create scatter plot
# Using petal length and petal width for visualization

plt.figure(figsize=(10, 6))

# Plot the data points
plt.scatter(
    X[:, 2],
    X[:, 3],
    c=labels,
    cmap="viridis",
    s=50
)

# Step 14: Plot cluster centers
plt.scatter(
    centers[:, 2],
    centers[:, 3],
    c="red",
    marker="X",
    s=200,
    label="Cluster Centers"
)

# Step 15: Add labels and title
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("K-Means Clustering of Iris Dataset")
plt.legend()

# Step 16: Display the final cluster visualization
plt.show()
