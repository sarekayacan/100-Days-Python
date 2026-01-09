#Hierarchical Clustering
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

X = np.array([
    [1, 2],
    [1, 4],
    [1, 0],
    [10, 2],
    [10, 4],
    [10, 0]
])

Z = linkage(X, method="ward")

plt.figure(figsize=(8, 4))
dendrogram(Z)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Veri Noktaları")
plt.ylabel("Mesafe")
plt.grid(True)
plt.show()

labels = fcluster(Z, t=5, criterion="distance")

print("Küme Etiketleri:", labels)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", s=100)
plt.title("Hierarchical Clustering Sonucu")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.grid(True)
plt.show()

# Bu dendrogram, hiyerarşik kümeleme sürecini görselleştirir.
# X ekseni veri noktalarını, Y ekseni ise kümelerin hangi mesafede birleştiğini gösterir. 
# Düşük mesafede birleşen noktalar birbirine daha benzerdir. 
# Grafikteki büyük mesafe sıçraması, kümeler arası belirgin fark olduğunu gösterir.
# Dendrogram bu seviyeden kesilerek uygun küme sayısının seçilmesini sağlar.
