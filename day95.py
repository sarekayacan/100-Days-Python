#PCA
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

X = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
    [5, 6, 7]
])

#PCA (2 bileşen)
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print("Açıklanan Varyans Oranı:", pca.explained_variance_ratio_)

#2D görselleştirme
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], s=100)
plt.title("PCA ile 3D Verinin 2D’ye İndirgenmesi")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.show()

# PCA, yüksek boyutlu verileri daha düşük boyutlu bir uzaya dönüştüren bir boyut indirgeme tekniğidir. 
# PCA, verideki maksimum varyansı yakalayan yönleri (principal components) belirler.
# Veri görselleştirme, gürültü azaltma ve makine öğrenmesi algoritmalarını hızlandırmak için yaygın olarak kullanılır.
# Açıklanan varyans oranı, verinin tamamının tek bir principal component tarafından açıklandığını göstermektedir.
# Bu durum, verinin gerçekte tek boyutlu bir yapı sergilediğini ve ikinci bileşenin bilgi taşımadığını ifade eder.
