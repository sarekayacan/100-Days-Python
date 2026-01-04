from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "dev"

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

with app.app_context():
    db.create_all()

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if not username or not email or not password:
            flash("Tüm alanlar zorunludur", "error")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)

        try:
            new_user = User(
                username=username,
                email=email,
                password=hashed_password
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Kayıt başarılı!", "success")
            return redirect(url_for("login"))
        except:
            db.session.rollback()
            flash("Kullanıcı adı veya email zaten var", "error")

    return render_template("register.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            flash("Giriş başarılı", "success")
            return redirect(url_for("profile"))
        else:
            flash("Hatalı email veya şifre", "error")

    return render_template("login.html")

# Profile
@app.route("/profile")
def profile():
    if "user_id" not in session:
        flash("Lütfen giriş yapın", "error")
        return redirect(url_for("login"))

    return render_template("profile.html", username=session["username"])

# Logout
@app.route("/logout")
def logout():
    session.clear()
    flash("Çıkış yapıldı", "success")
    return redirect(url_for("login"))

@app.route("/")
def home():
    return redirect(url_for("register"))

if __name__ == "__main__":
    app.run(debug=True)
