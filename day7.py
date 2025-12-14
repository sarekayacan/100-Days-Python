#Shopping List App
FILE_NAME = "liste.txt"

def load_list():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_list(shopping_list):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for item in shopping_list:
            file.write(item + "\n")


def show_menu():
    print("\n--- ALIŞVERİŞ LİSTESİ MENÜSÜ ---")
    print("1 - Listeyi görüntüle")
    print("2 - Ürün ekle")
    print("3 - Ürün sil")
    print("4 - Ürün düzenle")
    print("5 - Listeyi temizle")
    print("6 - Çıkış")


def display_list(shopping_list):
    if not shopping_list:
        print("\nListe boş.")
    else:
        print("\n--- ALIŞVERİŞ LİSTESİ ---")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")


def add_item(shopping_list):
    item = input("Eklenecek ürün: ").strip()
    if item:
        shopping_list.append(item)
        save_list(shopping_list)
        print(f"'{item}' listeye eklendi.")
    else:
        print("Geçersiz giriş!")


def remove_item(shopping_list):
    if not shopping_list:
        print("Liste boş!")
        return

    display_list(shopping_list)
    try:
        index = int(input("Silinecek ürün numarası: "))
        if 1 <= index <= len(shopping_list):
            removed = shopping_list.pop(index - 1)
            save_list(shopping_list)
            print(f"'{removed}' listeden silindi.")
        else:
            print("Geçersiz numara!")
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")


def edit_item(shopping_list):
    if not shopping_list:
        print("Liste boş!")
        return

    display_list(shopping_list)
    try:
        index = int(input("Düzenlenecek ürün numarası: "))
        if 1 <= index <= len(shopping_list):
            new_name = input("Yeni ürün adı: ").strip()
            if new_name:
                old_item = shopping_list[index - 1]
                shopping_list[index - 1] = new_name
                save_list(shopping_list)
                print(f"'{old_item}' → '{new_name}' olarak güncellendi.")
            else:
                print("Yeni isim boş olamaz!")
        else:
            print("Geçersiz numara!")
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")


def clear_list(shopping_list):
    shopping_list.clear()
    save_list(shopping_list)
    print("Liste temizlendi.")


def main():
    shopping_list = load_list()
    print("Alışveriş Listesi Uygulamasına Hoş Geldin!")

    while True:
        show_menu()
        choice = input("\nSeçimin: ")

        if choice == "1":
            display_list(shopping_list)
        elif choice == "2":
            add_item(shopping_list)
        elif choice == "3":
            remove_item(shopping_list)
        elif choice == "4":
            edit_item(shopping_list)
        elif choice == "5":
            clear_list(shopping_list)
        elif choice == "6":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim! 1-6 arası gir.")


main()
