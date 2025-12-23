#Countdown Timer
from datetime import datetime
#datetime(YIL, AY, GÜN, SAAT, DAKİKA, SANİYE)
import time
import json #etkinlikleri dosyaya kaydetmek ve okumak için

file_name = "events.json"

def load_events():
    try :
        with open(file_name,"r") as file: #dosya okuma modu
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_events(events):
    with open(file_name,"w") as file: #dosya yazma modu
        json.dump(events, file, indent=4) #Python sözlüğünü JSON formatında kaydeder,indent=4 okunabilirlik için
        
def add_event(events):
    name = input("Etkinlik adı: ")
    date_str = input("Tarih (YYYY-MM-DD HH:MM:SS): ")
    try:
        event_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        events[name] = date_str
        save_events(events)
        print("Etkinlik kaydedildi.")
    except ValueError:
        print("Tarih formatı hatalı!")
    
def show_events(events):
    if not events:
        print("Kayıtlı etkinlik yok.")
        return None

    print("\nEtkinlikler:")
    for i, name in enumerate(events, 1):
        print(f"{i}. {name} → {events[name]}")

    choice = int(input("Geri sayım yapılacak etkinlik numarası: "))
    selected = list(events.items())[choice - 1]
    return selected

def countdown(event_name, event_time):
    event_time = datetime.strptime(event_time, "%Y-%m-%d %H:%M:%S")
    while True:
        now = datetime.now()
        remaining = event_time - now

        if remaining.total_seconds() <= 0:
            print(f"\n{event_name} başladı!")
            break

        days = remaining.days
        hours, rem = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(rem, 60)

        print(
            f"\r⏳ {event_name} → "
            f"{days}g {hours}s {minutes}d {seconds}s",
            end=""
        ) #\r ifadesi aynı satırı günceller
        time.sleep(1) #1 saniye bekleme sağlar,geri sayımın her saniye güncellenmesi için

def main():
    events = load_events()

    while True:
        print("\nEtkinlik ekle")
        print("\nEtkinlikleri göster & geri sayım")
        print("\nÇıkış")

        choice = input("Seçim: ")

        if choice == "1":
            add_event(events)
        elif choice == "2":
            selected = show_events(events)
            if selected:
                countdown(*selected) #*selected tuple’ı parçalar
        elif choice == "3":
            print("Çıkış yapıldı.")
            break
        else:
            print("Geçersiz seçim!")

main()
