from datetime import datetime

FILE_NAME = "my_notes.txt"

def show_menu():
    print("\n--- NOT ALMA UYGULAMASI ---")
    print("1. Yeni not ekle")
    print("2. Tüm notları görüntüle")
    print("3. Not düzenle")
    print("4. Tüm notları sil")
    print("5. Notları dışa aktar (export)")
    print("6. Çıkış")


def add_note():
    note = input("Notunuzu girin: ")
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {note}\n")
    print("Not başarıyla eklendi.")


def view_notes():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            notes = file.readlines()

        if notes:
            print("\n--- NOTLARINIZ ---")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")
        else:
            print("Hiç not bulunamadı.")

    except FileNotFoundError:
        print("📭 Hiç not bulunamadı.")


def edit_note():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            notes = file.readlines()

        view_notes()
        index = int(input("Düzenlemek istediğiniz not numarasını girin: ")) - 1

        if 0 <= index < len(notes):
            new_note = input("Yeni not içeriğini girin: ")
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")
            notes[index] = f"[{timestamp}] {new_note}\n"

            with open(FILE_NAME, "w", encoding="utf-8") as file:
                file.writelines(notes)

            print("Not güncellendi.")
        else:
            print("Geçersiz numara.")

    except (FileNotFoundError, ValueError):
        print("Düzenlenecek not bulunamadı.")


def delete_notes():
    confirm = input("Tüm notları silmek istiyor musunuz? (yes/no): ")
    if confirm.lower() == "yes":
        open(FILE_NAME, "w").close()
        print("Tüm notlar silindi.")
    else:
        print("İşlem iptal edildi.")


def export_notes():
    export_file = "exported_notes.txt"
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as src:
            content = src.read()

        with open(export_file, "w", encoding="utf-8") as dest:
            dest.write(content)

        print(f"Notlar '{export_file}' dosyasına aktarıldı.")

    except FileNotFoundError:
        print("Aktarılacak not bulunamadı.")


while True:
    show_menu()
    choice = input("Seçiminiz (1-6): ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_notes()
    elif choice == "5":
        export_notes()
    elif choice == "6":
        print("Uygulamadan çıkılıyor. Görüşürüz!")
        break
    else:
        print("Geçersiz seçim.")
