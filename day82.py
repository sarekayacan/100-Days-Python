#Ridge and Lasso Regression
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

# Örnek veri
x = np.array([[750], [800], [850], [900], [950], [1000], [1050], [1100], [1150], [1200]])
y = np.array([150000, 160000, 165000, 170000, 180000, 190000, 195000, 200000, 210000, 220000])

# Veriyi eğitim ve test olarak ayırma
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=42)

ridge_model = Ridge(alpha=1.2)
ridge_model.fit(X_train, Y_train)
ridge_pred = ridge_model.predict(X_test)
ridge_mse = mean_squared_error(Y_test, ridge_pred)
print("Ridge MSE:", ridge_mse)

lasso_model = Lasso(alpha=0.1)
lasso_model.fit(X_train, Y_train)
lasso_pred = lasso_model.predict(X_test)
lasso_mse = mean_squared_error(Y_test, lasso_pred)
print("Lasso MSE:", lasso_mse)

plt.figure(figsize=(10,6))
plt.scatter(x, y, color='blue', label='Gerçek Veriler')
plt.plot(X_test, ridge_pred, color='red', marker='o', label='Ridge Tahminleri')
plt.plot(X_test, lasso_pred, color='green', marker='x', label='Lasso Tahminleri')
plt.title('Ridge ve Lasso Regresyon Tahminleri')
plt.xlabel('Ev Alanı')
plt.ylabel('Ev Fiyatı')
plt.legend()
plt.grid(True)
plt.show()
