#K Means Clustering
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Veri seti
X = np.array([
    [1, 2],
    [1, 4],
    [1, 0],
    [10, 2],
    [10, 4],
    [10, 0]
])
#Model
kmeans = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)
#Eğitme
kmeans.fit(X)
#Sonuçlar
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
#Görselleştirme
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", s=100, label="Data Points")
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    c="red",
    marker="X",
    s=300,
    label="Centroids"
)

plt.title("K-Means Kümeleme")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.legend()
plt.grid(True)
plt.show()
