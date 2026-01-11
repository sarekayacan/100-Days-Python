#Simple Recommendation System
import nltk
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Eğitim verisi (basit bilgi tabanı)
corpus = [
    "hello",
    "hi",
    "hey",
    "i am a chatbot",
    "my name is python bot",
    "python is a programming language used for data science machine learning and web development",
    "python is easy to learn and very powerful",
    "machine learning is a part of artificial intelligence",
    "nlp stands for natural language processing",
    "artificial intelligence is the future",
    "bye",
    "goodbye",
]

# Metin temizleme fonksiyonu
def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens

# Selamlama yanıtları
greeting_inputs = ["hello", "hi", "hey", "greetings"]
greeting_responses = ["Hello!", "Hi there!", "Hey!", "Hello, how can I help?"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greeting_inputs:
            return random.choice(greeting_responses)
    return None

def rule_based_response(text):
    if "python" in text:
        return "Python is a popular programming language used in software development, data science and AI."
    if "nlp" in text:
        return "NLP stands for Natural Language Processing."
    return None

# Chatbot yanıt üretme
def chatbot_response(user_input):
    corpus.append(user_input)

    vectorizer = TfidfVectorizer(tokenizer=preprocess, stop_words='english')
    tfidf = vectorizer.fit_transform(corpus)

    similarity = cosine_similarity(tfidf[-1], tfidf)
    index = similarity.argsort()[0][-2]

    flat = similarity.flatten()
    flat.sort()
    score = flat[-2]

    corpus.pop()

    if score < 0.2:
        return "I am not sure about that. Can you ask differently?"
    else:
        return corpus[index]

# Ana döngü
print("Python NLP Chatbot")
print("Type 'bye' to exit")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot: Goodbye!")
        break

    greet = greeting(user_input)
    if greet:
        print("Bot:", greet)
    else:
        rule = rule_based_response(user_input)
        if rule:
            print("Bot:", rule)
        else:
            print("Bot:", chatbot_response(user_input))
