#Fake News Detector
import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

#NLTK kaynakları
nltk.download("punkt")
nltk.download("stopwords")

#Dataset yükleme
url = "https://raw.githubusercontent.com/lutzhamel/fake-news/master/data/fake_or_real_news.csv"
df = pd.read_csv(url)

#Metin temizleme fonksiyonu
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

#Temiz metin oluşturma
df["clean_text"] = df["text"].apply(clean_text)

#Label dönüşümü (SORUNSUZ)
df["label"] = df["label"].str.lower().str.strip()
df["label"] = df["label"].map({"real": 1, "fake": 0})

#TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df["clean_text"])
y = df["label"]

#Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#Logistic Regression Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

#Değerlendirme
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

#Tahmin fonksiyonu
def predict_news(news_text):
    cleaned = clean_text(news_text)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    return "GERÇEK HABER" if prediction == 1 else "SAHTE HABER"

#Test
test_news = "Breaking news: Scientists discover a new cure for cancer"
print("\nTest Sonucu:", predict_news(test_news))
