#Global Weather Dashboard 
import requests
import matplotlib.pyplot as plt

API_KEY = "bcf1017dfd543aac60fad940f1abf3c9"
BASE_URL_CURRENT = "https://api.openweathermap.org/data/2.5/weather"
BASE_URL_FORECAST = "https://api.openweathermap.org/data/2.5/forecast"

def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "tr"
    }

    response = requests.get(BASE_URL_CURRENT, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def fetch_hourly_forecast(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "tr"
    }

    response = requests.get(BASE_URL_FORECAST, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data):
    print("\nŞehir:", data["name"])
    print("Sıcaklık:", data["main"]["temp"], "°C")
    print("Durum:", data["weather"][0]["description"])
    print("Nem:", data["main"]["humidity"], "%")
    print("Rüzgar:", data["wind"]["speed"], "m/s")

def plot_hourly_forecast(forecast_data, city):
    hours = []
    temps = []

    for item in forecast_data["list"][:8]:  # ilk 24 saat (3 saatlik)
        hours.append(item["dt_txt"][11:16])
        temps.append(item["main"]["temp"])

    plt.plot(hours, temps, marker="o")
    plt.title(f"{city} - Saatlik Sıcaklık Tahmini")
    plt.xlabel("Saat")
    plt.ylabel("°C")
    plt.grid(True)
    plt.show()
    
def compare_cities(cities):
    city_names = []
    temps = []

    for city in cities:
        data = fetch_weather(city)
        if data:
            city_names.append(data["name"])
            temps.append(data["main"]["temp"])

    plt.bar(city_names, temps)
    plt.title("Şehirler Arası Sıcaklık Karşılaştırması")
    plt.ylabel("°C")
    plt.show()

def main():
    print("GLOBAL WEATHER DASHBOARD")

    while True:
        print("\n1 - Tek şehir hava durumu")
        print("2 - Şehirleri karşılaştır")
        print("3 - Çıkış")

        choice = input("Seçimin: ")

        if choice == "1":
            city = input("Şehir adı gir: ").strip()
            data = fetch_weather(city)

            if data:
                display_weather(data)

                forecast = fetch_hourly_forecast(city)
                if forecast:
                    plot_hourly_forecast(forecast, city)
            else:
                print("Veri alınamadı")

        elif choice == "2":
            cities = input("Şehirleri virgülle gir: ").split(",")
            cities = [c.strip() for c in cities]
            compare_cities(cities)

        elif choice == "3":
            print("Görüşürüz!")
            break

        else:
            print("Geçersiz seçim")
            
if __name__ == "__main__": #Bu dosya direkt çalıştırıldıysa main() fonksiyonunu çalıştır.
    main()
