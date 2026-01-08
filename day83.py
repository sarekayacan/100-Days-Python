#Polynomial Regression
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([15, 18, 21, 25, 30, 36, 43, 51, 60, 70])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model = LinearRegression()
model.fit(X_train_poly, y_train)

y_pred = model.predict(X_test_poly)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error (MSE):", mse)
print("Tahmin edilen maaşlar:", y_pred)

plt.scatter(X, y, color='red', label='Gerçek Veri') 

X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
X_range_poly = poly.transform(X_range)
y_range_pred = model.predict(X_range_poly)

plt.plot(X_range, y_range_pred, color='blue', label='Polinomsal Regresyon')  
plt.title("Deneyim vs Maaş (Polinomsal Regresyon)")
plt.xlabel("Deneyim (Yıl)")
plt.ylabel("Maaş (Bin TL)")
plt.legend()
plt.show()
