#Isolation Forest
from sklearn.ensemble import IsolationForest
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]
X_test = np.r_[
    X + 2,
    X - 2,
    np.random.uniform(low=-6, high=6, size=(20, 2))
]

model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X_train)

y_pred = model.predict(X_test)

normal = X_test[y_pred == 1]
anomaly = X_test[y_pred == -1]

plt.figure(figsize=(8, 6))
plt.scatter(
    normal[:, 0], normal[:, 1],
    label="Normal",
    alpha=0.7
)
plt.scatter(
    anomaly[:, 0], anomaly[:, 1],
    label="Anomaly",
    marker="x",
    s=100
)
plt.title("Isolation Forest Anomaly Detection")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True)
plt.show()

# Bu görselleştirme, Isolation Forest algoritmasının anomalileri nasıl tespit ettiğini göstermektedir.
# Sonuçlar, Isolation Forest’ın anomali tespitinde dağılım yoğunluğunu temel alan çalışma prensibiyle uyumludur.