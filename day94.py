#GMM
import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

X = np.array([
    [1, 2],
    [2, 2],
    [2, 3],
    [8, 7],
    [8, 8],
    [25, 80]
])

gmm = GaussianMixture(
    n_components=2,
    random_state=42,
    covariance_type="full"
)

labels = gmm.fit_predict(X)
probabilities = gmm.predict_proba(X)

print("Küme Etiketleri:", labels)
print("\nKüme Olasılıkları:\n", probabilities)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", s=100)
plt.title("Gaussian Mixture Model (GMM) Kümeleme")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.grid(True)
plt.show()

# Çıktıya göre GMM algoritması iki küme tespit etmiştir.
# İlk beş veri noktası birinci kümeye, son veri noktası ise ikinci kümeye yüksek olasılıkla atanmıştır. 
# Olasılıkların 1 ve 0 çıkması, kümelerin birbirinden net şekilde ayrıldığını ve örtüşme olmadığını göstermektedir.
