#t-SNE
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

#3D örnek veri seti
X = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
    [5, 6, 7],
    [8, 5, 7],
    [9, 6, 8]
])

#t-SNE modeli
tsne = TSNE(
    n_components=2,
    perplexity=5,
    random_state=42
)

#Boyut indirgeme
X_reduced = tsne.fit_transform(X)

print("t-SNE ile indirgenmiş veri:\n", X_reduced)

plt.figure()
plt.scatter(X_reduced[:, 0], X_reduced[:, 1])
plt.title("t-SNE ile 3D Verinin 2D'ye İndirgenmesi")
plt.xlabel("t-SNE Bileşen 1")
plt.ylabel("t-SNE Bileşen 2")
plt.grid(True)
plt.show()

# t-SNE, yüksek boyutlu verileri 2D veya 3D uzaya indirgemek için kullanılan doğrusal olmayan bir boyut indirgeme yöntemidir. 
# PCA'dan farklı olarak varyansı değil, veri noktaları arasındaki yerel komşuluk ilişkilerini korur.
# Bu nedenle özellikle veri görselleştirme ve küme yapılarının keşfi için etkilidir.
