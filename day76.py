#Simple Recommendation System
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

products = {
    "Product": [
        "Python Course",
        "Machine Learning Course",
        "Deep Learning Course",
        "Data Science Course",
        "AI Course"
    ],
    "Category": [
        "programming python",
        "machine learning ai",
        "deep learning neural networks",
        "data science analytics",
        "artificial intelligence ai"
    ]
}

df = pd.DataFrame(products)

vectorizer = TfidfVectorizer()
category_vectors = vectorizer.fit_transform(df["Category"])
similarity_matrix = cosine_similarity(category_vectors)

def recommend_product(product_name):
    product_name = product_name.lower().strip()

    df_lower = df.copy()
    df_lower["Product"] = df_lower["Product"].str.lower().str.strip()

    if product_name not in df_lower["Product"].values:
        return ["Ürün bulunamadı"]

    index = df_lower[df_lower["Product"] == product_name].index[0]

    scores = list(enumerate(similarity_matrix[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = [
        df["Product"][i]   
        for i, score in scores[1:3]
    ]
    return recommendations

ratings = {
    "User": ["Alice", "Bob", "Charlie", "David"],
    "Python Course": [5, 3, 4, 0],
    "ML Course": [4, 5, 3, 4],
    "AI Course": [5, 4, 0, 5],
    "Data Science Course": [0, 4, 5, 3]
}

ratings_df = pd.DataFrame(ratings).set_index("User")
user_similarity = cosine_similarity(ratings_df.fillna(0))
np.fill_diagonal(user_similarity, 0)

user_similarity_df = pd.DataFrame(
    user_similarity,
    index=ratings_df.index,
    columns=ratings_df.index
)

def recommend_for_user(user):
    user = user.lower()

    index_lower = ratings_df.index.str.lower()
    
    if user not in index_lower:
        return ["Kullanıcı bulunamadı"]

    real_user = ratings_df.index[index_lower == user][0]

    similar_user = user_similarity_df[real_user].idxmax()
    recommendations = ratings_df.loc[similar_user]

    return recommendations[recommendations >= 4].index.tolist()

def content_based_action():
    product = product_entry.get()
    result = recommend_product(product)
    messagebox.showinfo("Öneriler", "\n".join(result))

def collaborative_action():
    user = user_entry.get()
    result = recommend_for_user(user)
    messagebox.showinfo("Öneriler", "\n".join(result))

root = tk.Tk()
root.title("Simple Recommendation System")
root.geometry("400x300")

tk.Label(root, text="İçerik Tabanlı Öneri", font=("Arial", 12, "bold")).pack(pady=5)
product_entry = tk.Entry(root)
product_entry.pack()
tk.Button(root, text="Ürün Öner", command=content_based_action).pack(pady=5)

tk.Label(root, text="Kullanıcı Tabanlı Öneri", font=("Arial", 12, "bold")).pack(pady=10)
user_entry = tk.Entry(root)
user_entry.pack()
tk.Button(root, text="Kullanıcıya Öner", command=collaborative_action).pack(pady=5)

root.mainloop()
