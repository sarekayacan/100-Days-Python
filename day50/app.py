from flask import Flask, render_template, request, session
import requests

app = Flask(__name__)
app.secret_key = "weather_secret_key"

API_KEY = "API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
ICON_URL = "https://openweathermap.org/img/wn/{}@2x.png"

def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "tr"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def parse_weather(data):
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"].title(),
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "icon": ICON_URL.format(data["weather"][0]["icon"])
    }

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        city = request.form.get("city")
        data = fetch_weather(city)

        if data.get("cod") != 200:
            error = "Şehir bulunamadı. Lütfen tekrar deneyin."
        else:
            weather = parse_weather(data)
            if city not in session["history"]:
                session["history"].append(city)

    return render_template(
        "index.html",
        weather=weather,
        error=error,
        history=session["history"]
    )

if __name__ == "__main__":
    app.run(debug=True)
