#One-Class SVM
import numpy as np
from sklearn.svm import OneClassSVM

np.random.seed(42)

X = 0.3 * np.random.randn(100, 2)

X_train = np.r_[X + 2, X - 2]
X_test = np.r_[X + 2, X - 2]

X_outliers = np.random.uniform(low=-6, high=6, size=(20, 2))

model = OneClassSVM(
    kernel="rbf",
    gamma="auto",
    nu=0.1
)
model.fit(X_train)

pred_test = model.predict(X_test)
pred_outliers = model.predict(X_outliers)

print("Normal Veri Tahminleri (1 = normal, -1 = anomali):")
print(pred_test)

print("\nAykırı Veri Tahminleri (1 = normal, -1 = anomali):")
print(pred_outliers)

# Bu uygulamada One-Class SVM algoritması kullanılarak normal veri dağılımı öğrenilmiştir.
# Bu dağılımdan önemli ölçüde sapan noktalar anomali olarak tespit edilmiştir.
