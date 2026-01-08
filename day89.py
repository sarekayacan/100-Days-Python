#Gradient Boosting
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

#Örnek veri: [çalışma saati, önceki not]
X = np.array([
    [5, 70],
    [3, 50],
    [8, 90],
    [2, 30],
    [4, 60],
    [6, 80],
    [1, 20],
    [7, 85],
    [3, 40],
    [5, 75]
])

y = np.array([1, 0, 1, 0, 1, 1, 0, 1, 0, 1])

#Eğitim ve test setine ayır (Stratify ile sınıf dengesini koruyoruz)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42, stratify=y
)

#Gradient Boosting modeli
model = GradientBoostingClassifier(
    n_estimators=100,  
    learning_rate=0.1, 
    random_state=42
)
#Modeli eğit
model.fit(X_train, y_train)

#Tahmin yap
y_pred = model.predict(X_test)

#Performans ölçümü
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred, labels=[0,1])

print(f"Model Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(conf_matrix)
