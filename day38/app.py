from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp
import csv
import os

app = Flask(__name__)
app.secret_key = "super_secret_key"

CSV_FILE = "submissions.csv"


class ContactForm(FlaskForm):
    name = StringField("İsim", validators=[DataRequired()])
    email = StringField("E-posta", validators=[DataRequired(), Email()])
    phone = StringField(
        "Telefon",
        validators=[
            DataRequired(),
            Regexp(r"^[0-9]{10,11}$", message="Geçerli bir telefon numarası giriniz")
        ]
    )
    message = TextAreaField("Mesaj", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("Mesaj Gönder")


@app.route("/", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        save_to_csv(
            form.name.data,
            form.email.data,
            form.phone.data,
            form.message.data
        )

        flash(f"Teşekkürler {form.name.data}, mesajınız başarıyla gönderildi.", "success")
        return redirect(url_for("success"))

    return render_template("contact.html", form=form)


@app.route("/success")
def success():
    return render_template("success.html")


def save_to_csv(name, email, phone, message):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["İsim", "E-posta", "Telefon", "Mesaj"])

        writer.writerow([name, email, phone, message])


if __name__ == "__main__":
    app.run(debug=True)
