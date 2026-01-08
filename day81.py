#Linear Regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt  # Grafik çizmek için

# 1. Veri
X = np.array([[50], [60], [70], [80], [90], [100], [110], [120], [130], [140]])
Y = np.array([150000, 180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000])

# 2. Veriyi eğitim ve test olarak böl
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 3. Modeli oluştur ve eğit
model = LinearRegression()
model.fit(X_train, Y_train)

# 4. Tahmin yap
Y_pred = model.predict(X_test)

# 5. Modeli değerlendir
mse = mean_squared_error(Y_test, Y_pred)
print("Ortalama Kare Hatası (MSE):", mse)
print("Tahmin Edilen Değerler:", Y_pred)

# 6. Grafik çiz
plt.scatter(X, Y, color='blue', label='Gerçek Fiyatlar')  # Gerçek veriler
plt.plot(X, model.predict(X), color='red', label='Tahmin Edilen Doğru Çizgi')  # Doğru çizgi
plt.xlabel('Ev Büyüklüğü (m²)')
plt.ylabel('Ev Fiyatı')
plt.title('Ev Büyüklüğü ve Fiyatı Arasındaki Doğrusal İlişki')
plt.legend()
plt.show()
