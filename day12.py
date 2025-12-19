#Temperature Conversion Functions
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32

def menu():
    print("\n--- Sıcaklık Dönüştürücü ---")
    print("1. Celsius → Fahrenheit & Kelvin")
    print("2. Fahrenheit → Celsius & Kelvin")
    print("3. Kelvin → Celsius & Fahrenheit")
    print("4. Tüm Birimlere Otomatik Dönüştür")
    print("5. Çıkış")
    
    choice = input("Seçiminizi girin (1-5): ")

    if choice == "5":
        print("Programdan çıkılıyor.")
        return

    decimal = int(input("Kaç ondalık basamak istiyorsunuz?: "))
    
    if choice == "1":
        values = input("Celsius değerlerini girin (virgülle ayırın): ").split(",")
        for v in values:
            c = float(v)
            print(f"\nCelsius: {c}")
            print(f"Fahrenheit: {celsius_to_fahrenheit(c):.{decimal}f}")
            print(f"Kelvin: {celsius_to_kelvin(c):.{decimal}f}")

    elif choice == "2":
        values = input("Fahrenheit değerlerini girin (virgülle ayırın): ").split(",")
        for v in values:
            f = float(v)
            print(f"\nFahrenheit: {f}")
            print(f"Celsius: {fahrenheit_to_celsius(f):.{decimal}f}")
            print(f"Kelvin: {fahrenheit_to_kelvin(f):.{decimal}f}")

    elif choice == "3":
        values = input("Kelvin değerlerini girin (virgülle ayırın): ").split(",")
        for v in values:
            k = float(v)
            print(f"\nKelvin: {k}")
            print(f"Celsius: {kelvin_to_celsius(k):.{decimal}f}")
            print(f"Fahrenheit: {kelvin_to_fahrenheit(k):.{decimal}f}")

    elif choice == "4":
        temp = float(input("Sıcaklık değerini girin: "))
        unit = input("Birim girin (C / F / K): ").upper()

        if unit == "C":
            print(f"Fahrenheit: {celsius_to_fahrenheit(temp):.{decimal}f}")
            print(f"Kelvin: {celsius_to_kelvin(temp):.{decimal}f}")

        elif unit == "F":
            print(f"Celsius: {fahrenheit_to_celsius(temp):.{decimal}f}")
            print(f"Kelvin: {fahrenheit_to_kelvin(temp):.{decimal}f}")

        elif unit == "K":
            print(f"Celsius: {kelvin_to_celsius(temp):.{decimal}f}")
            print(f"Fahrenheit: {kelvin_to_fahrenheit(temp):.{decimal}f}")

        else:
            print("Geçersiz birim.")

    else:
        print("Geçersiz seçim!")
    menu()

menu()
