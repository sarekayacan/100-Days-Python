#Text Sentiment Analyzer
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tkinter as tk
from tkinter import messagebox

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

def analyze_sentiment_vader(text):
    score = analyzer.polarity_scores(text)['compound']
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def run_gui():
    def analyze():
        text = entry.get().strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter a sentence!")
            return
        tb_result = analyze_sentiment_textblob(text)
        vader_result = analyze_sentiment_vader(text)

        popup = tk.Toplevel(root)
        popup.title("Analysis Result")
        popup.geometry("300x150")
        tk.Label(popup, text="Sentiment Analysis Results", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Label(popup, text=f"TextBlob: {tb_result}", font=("Arial", 12)).pack(pady=5)
        tk.Label(popup, text=f"Vader: {vader_result}", font=("Arial", 12)).pack(pady=5)
        tk.Button(popup, text="Close", command=popup.destroy).pack(pady=10)

    root = tk.Tk()
    root.title("English Text Sentiment Analyzer")
    root.geometry("500x200")

    tk.Label(root, text="Enter a sentence for sentiment analysis:", font=("Arial", 12)).pack(pady=10)
    entry = tk.Entry(root, width=60, font=("Arial", 12))
    entry.pack(pady=8)

    tk.Button(root, text="Analyze", command=analyze, font=("Arial", 12)).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
