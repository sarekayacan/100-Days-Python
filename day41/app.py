from flask import Flask, render_template
import os

app = Flask(__name__)

# Environment variable (bonus)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "default_secret")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
