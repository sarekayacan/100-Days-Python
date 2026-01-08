#Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
Y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)
cm = confusion_matrix(Y_test, Y_pred)

print("Doğruluk oranı (Accuracy):", accuracy)
print("Confusion Matrix (Karışıklık Matrisi):\n", cm)

X_range = np.linspace(0, 12, 300).reshape(-1, 1)  
Y_prob = model.predict_proba(X_range)[:, 1]      

plt.figure(figsize=(8,5))
plt.scatter(X, Y, color='red', label='Gerçek veri') 
plt.plot(X_range, Y_prob, color='blue', label='Sigmoid eğrisi')  
plt.title("Çalışma Saatine Göre Geçme Olasılığı")
plt.xlabel("Çalışma Saati")
plt.ylabel("Geçme Olasılığı")
plt.legend()
plt.grid(True)
plt.show()
