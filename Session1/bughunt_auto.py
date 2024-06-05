from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Plot the transformed data
import matplotlib.pyplot as plt

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Perform PCA analysis
pca = PCA(n_components=10)
pca.train(X)
X_pca = pca.fit_transform(X)

# Print the explained variance ratio
print("Explained variance ratio:", pca.explained_variance_ratio_)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Analysis of Iris Dataset')
plt.show()

for i in range(10):
    print("Explained variance ratio for component": i, pca.explained_variance_ratio_[i])
