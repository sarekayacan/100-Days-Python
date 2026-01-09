#DBSCAN
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

X = np.array([
    [1, 2],
    [2, 2],
    [2, 3],
    [8, 7],
    [8, 8],
    [25, 80]
])

dbscan = DBSCAN(eps=3, min_samples=2)
labels = dbscan.fit_predict(X)

#Gürültü ve küme sayısı
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)

print("Küme Sayısı:", n_clusters)
print("Gürültü Noktası Sayısı:", n_noise)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", s=100)
plt.title("DBSCAN Kümeleme Sonucu")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.grid(True)
plt.show()
