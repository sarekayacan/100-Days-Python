#Spam Email Detector
import pandas as pd
import re
import nltk
import tkinter as tk
from tkinter import messagebox
import os

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

nltk.download("stopwords")
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    text = re.sub(r"\W", " ", text)
    text = text.lower()
    words = text.split()
    words = [stemmer.stem(w) for w in words if w not in stop_words]
    return " ".join(words)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "spam.csv")
df = pd.read_csv(csv_path, encoding="latin-1", sep=";")
df = df.iloc[:, :2]
df.columns = ["label", "message"]

df["label"] = df["label"].map({"ham": 0, "spam": 1})
df["clean_message"] = df["message"].apply(preprocess_text)

print(df["label"].value_counts())

vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(df["clean_message"])
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Model Accuracy: %{accuracy*100:.2f}")

def predict_email(text):
    processed = preprocess_text(text)
    vectorized = vectorizer.transform([processed])
    prediction = model.predict(vectorized)[0]
    return "SPAM" if prediction == 1 else "SPAM DEĞİL"

def check_spam():
    email = text_box.get("1.0", tk.END).strip()
    if not email:
        messagebox.showwarning("Uyarı", "Lütfen bir e-posta girin.")
        return
    result = predict_email(email)
    result_label.config(text=f"Sonuç: {result}")

window = tk.Tk()
window.title("Spam E-posta Tespit Uygulaması")
window.geometry("500x350")

tk.Label(window, text="E-posta Metni:", font=("Arial", 12)).pack(pady=5)

text_box = tk.Text(window, height=8, width=55)
text_box.pack()

tk.Button(window, text="Kontrol Et", command=check_spam, font=("Arial", 11)).pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

window.mainloop()
