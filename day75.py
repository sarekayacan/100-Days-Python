#Kripto Para Tracker
import requests

def get_crypto_data(coin):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "ids": coin.lower()}
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        return None
    
    data = response.json()
    if len(data) == 0:
        return None
    
    coin_info = data[0]
    name = coin_info["name"]
    price = coin_info["current_price"]
    change_24h = coin_info["price_change_percentage_24h"]
    
    if change_24h > 5:
        trend = "Çok hızlı artış!"
    elif change_24h > 0:
        trend = "Artış"
    elif change_24h < -5:
        trend = "Çok hızlı düşüş!"
    else:
        trend = "Azalış" if change_24h < 0 else "Değişim yok"
    
    return f"{name} fiyatı: ${price:.2f} (24 saat: {change_24h:.2f}%) → {trend}"

def main():
    print("=== Kripto Para Tracker ===")
    print("Örnek kriptolar: bitcoin, ethereum, ripple, dogecoin, cardano")
    print("Üç farklı kriptoyu aralarında virgül ile yazabilirsiniz.")
    
    coins_input = input("Hangi kripto paraları görmek istiyorsunuz? ").strip()
    coins = [c.strip() for c in coins_input.split(",")][:3]  
    
    print("\n--- Sonuçlar ---\n")
    for coin in coins:
        result = get_crypto_data(coin)
        if result:
            print(result)
        else:
            print(f"{coin} için veri bulunamadı veya API hatası oluştu.")

if __name__ == "__main__":
    main()
