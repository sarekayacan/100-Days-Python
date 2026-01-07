#Portfolio Website
from flask import Flask, render_template, request, redirect, url_for, Response
import json
import os

app = Flask(__name__)

FEEDBACK_FILE = "feedback.json"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"


def load_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        return []
    with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_feedback(name, email, message):
    data = load_feedback()

    #Aynı email tekrar göndermesin
    for feedback in data:
        if feedback["email"] == email:
            return False

    data.append({
        "name": name,
        "email": email,
        "message": message
    })

    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return True


def check_auth(username, password):
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD


def authenticate():
    return Response(
        "Yetkisiz erişim!", 401,
        {"WWW-Authenticate": 'Basic realm="Admin Panel"'}
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit-feedback", methods=["POST"])
def submit_feedback():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    success = save_feedback(name, email, message)

    if not success:
        return "Bu e-posta ile daha önce geri bildirim gönderilmiş!"

    return "Geri bildirim başarıyla gönderildi!"

@app.route("/feedback")
def feedback():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()

    search_query = request.args.get("q", "").lower()
    feedbacks = load_feedback()

    #Arama filtresi
    if search_query:
        feedbacks = [
            f for f in feedbacks
            if search_query in f["name"].lower()
            or search_query in f["email"].lower()
            or search_query in f["message"].lower()
        ]

    return render_template("feedback.html", feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(debug=True)
