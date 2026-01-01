#Weather App Using API
import requests
from datetime import datetime

API_KEY = "API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"
LOG_FILE = "weather_log.txt"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("City not found or API error.")
        return None

    data = response.json()

    weather = {
        "City": data["name"],
        "Temperature (°C)": data["main"]["temp"],
        "Humidity (%)": data["main"]["humidity"],
        "Weather": data["weather"][0]["description"].title(),
        "Wind Speed (m/s)": data["wind"]["speed"],
        "Sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M"),
        "Sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")
    }

    return weather


def get_5_day_forecast(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(FORECAST_URL, params=params)

    if response.status_code != 200:
        print("Forecast not available.")
        return []

    data = response.json()
    forecast_list = []

    for item in data["list"][::8]:  
        forecast_list.append({
            "Date": item["dt_txt"].split(" ")[0],
            "Temp": item["main"]["temp"],
            "Weather": item["weather"][0]["description"].title()
        })

    return forecast_list


def save_to_file(weather, forecast):
    with open(LOG_FILE, "a") as file:
        file.write("\n--- Weather Report ---\n")
        for key, value in weather.items():
            file.write(f"{key}: {value}\n")

        file.write("\n5 Day Forecast:\n")
        for day in forecast:
            file.write(
                f"{day['Date']} | {day['Temp']}°C | {day['Weather']}\n"
            )

        file.write("-" * 30 + "\n")


def display_weather(weather, forecast):
    print("\n--- Current Weather ---")
    for key, value in weather.items():
        print(f"{key}: {value}")

    print("\n--- 5 Day Forecast ---")
    for day in forecast:
        print(
            f"{day['Date']} | {day['Temp']}°C | {day['Weather']}"
        )

def main():
    while True:
        city = input("\nEnter city name (or Q to quit): ").strip()

        if city.lower() == "q":
            print("Goodbye ")
            break

        weather = get_weather(city)
        if not weather:
            continue

        forecast = get_5_day_forecast(city)

        display_weather(weather, forecast)
        save_to_file(weather, forecast)
        print("\nWeather data saved to file.")


main()
