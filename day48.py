import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

def fetch_page(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}) #Yahoo Finance botları engellediği için User-Agent ekliyoruz
        if response.status_code == 200:
            return response.text
        else:
            print(f"Sayfa alınamadı. Hata kodu: {response.status_code}")
            return None
    except Exception as e:
        print("Bağlantı hatası:", e)
        return None

def parse_html(html):
    return BeautifulSoup(html, "html.parser") #HTML artık Python objesi

def get_stock_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    html = fetch_page(url)

    if not html:
        return None

    soup = BeautifulSoup(html, "html.parser")

    price_tag = soup.find("fin-streamer", {"data-field": "regularMarketPrice"})

    if price_tag:
        return price_tag.text.strip()
    else:
        return None


def track_stocks(tickers, interval):
    print("\nTakip başlatıldı (Ctrl + C ile durdurabilirsiniz)\n")

    while True:
        print("-" * 40)
        print(datetime.now().strftime("%H:%M:%S"))

        for ticker in tickers:
            price = get_stock_price(ticker)
            if price:
                print(f"{ticker}: ${price}")
            else:
                print(f"{ticker}: veri yok")

        time.sleep(interval)

def main():
    print("STOCK PRICE TRACKER")

    tickers_input = input("Hisse sembollerini gir (virgülle ayır): ")
    tickers = [t.strip().upper() for t in tickers_input.split(",")]

    interval = int(input("Güncelleme aralığı (saniye): "))

    track_stocks(tickers, interval)

if __name__ == "__main__":
    main()
