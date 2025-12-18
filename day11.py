#Safe Calculator 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Sıfıra bölme yapılamaz!")
    return x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y


def show_menu():
    print("\n--- GÜVENLİ HESAP MAKİNESİ ---")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Mod Alma")
    print("6. Üs Alma")
    print("7. Çıkış")


def log_error(error):
    with open("error_log.txt", "a") as file:
        file.write(str(error) + "\n")

while True:
    show_menu()
    choice = input("Seçiminizi yapın (1-7): ")

    if choice == "7":
        print("Hesap makinesi kapatılıyor.")
        break

    try:
        num1 = float(input("Birinci sayı: "))
        num2 = float(input("İkinci sayı: "))

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        elif choice == "5":
            result = modulus(num1, num2)
        elif choice == "6":
            result = power(num1, num2)
        else:
            print("Geçersiz seçim!")
            continue

        print("Sonuç:", result)

    except ValueError:
        print("Hata: Lütfen geçerli sayılar girin.")
        log_error("ValueError: Geçersiz giriş")

    except ZeroDivisionError as e:
        print("Hata:", e)
        log_error(e)

    except Exception as e:
        print("Beklenmeyen bir hata oluştu.")
        log_error(e)

    finally:
        print("İşlem tamamlandı.")
        
