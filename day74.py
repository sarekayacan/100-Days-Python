#WeatherWise
import requests

def normalize_city(city_name):
    turkish_chars = "çğıöşüÇĞİÖŞÜ"
    replacement = "cgiosuCGIOSU"
    for t, r in zip(turkish_chars, replacement):
        city_name = city_name.replace(t, r)
    return city_name

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&lang=tr&appid={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Hata: Şehir bulunamadı veya API hatası.")
        return None
    data = response.json()
    
    forecast = []
    days_collected = set()
    
    for item in data["list"]:
        date = item["dt_txt"].split(" ")[0]  
        if date not in days_collected:
            condition = item["weather"][0]["description"].capitalize()
            temp = round(item["main"]["temp"])
            
            advice = ""
            if "yağmur" in condition.lower():
                advice = "Şemsiye yanınıza almayı unutmayın."
            elif "kar" in condition.lower():
                advice = "Kalın mont ve bot giymeniz iyi olur."
            elif "güneş" in condition.lower():
                advice = "Güneş kremi sürmeyi unutmayın."
            else:
                advice = "Hafif bir mont yeterli olacaktır."
            
            forecast.append({
                "Tarih": date,
                "Hava": condition,
                "Sıcaklık (°C)": temp,
                "Tavsiye": advice
            })
            days_collected.add(date)
        if len(forecast) == 3: 
            break
    return forecast

def display_forecast(city_name, forecast):
    """
    Şehre ait hava tahminini ekrana yazdırır.
    """
    print(f"\n{city_name.title()} için 3 Günlük Hava Tahmini:\n")
    for day in forecast:
        print(f"{day['Tarih']}: {day['Hava']}, {day['Sıcaklık (°C)']}°C")
        print(f"Tavsiye: {day['Tavsiye']}\n")

print("HavaRehberi Programına Hoşgeldiniz!\n")
city_input = input("Lütfen şehir ismini girin: ").strip()

if not city_input:
    print("Hata: Şehir ismi boş bırakılamaz.")
else:
    normalized_city = normalize_city(city_input)
    
    API_KEY = "BURAYA_API_KEYİNİZİ_YAZIN"
    
    forecast = get_weather(normalized_city, API_KEY)
    
    if forecast:
        display_forecast(normalized_city, forecast)
