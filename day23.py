#Library Management System
import json
from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.due_date = None  #ödünç alınan kitap için son tarih
        
    def display_info(self):
        status = "Ödünç alınabilir" if not self.is_borrowed else f"Ödünç alınmış, son tarih: {self.due_date.strftime('%d-%m-%Y')}"
        print(f"Başlık: {self.title} | Yazar: {self.author} | Durum: {status}")
        
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Kitap eklendi: '{title}' - {author}")
        
    def view_books(self):
        if not self.books:
            print("Kütüphanede kitap yok.")
            return
        print("\n--- Kütüphane Kitapları ---")
        for book in self.books:
            book.display_info()
            
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                book.due_date = datetime.now() + timedelta(days=14)  # 14 gün süreli ödünç
                print(f"'{book.title}' ödünç alındı. Son iade tarihi: {book.due_date.strftime('%d-%m-%Y')}")
                return
        print(f"'{title}' kitap ödünç alınamaz veya kütüphanede yok.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                book.due_date = None
                print(f"'{book.title}' iade edildi. Teşekkürler!")
                return
        print(f"'{title}' kütüphanede bulunamadı veya ödünç alınmamış.")

    def search_book(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if not results:
            print(f"'{keyword}' ile eşleşen kitap bulunamadı.")
            return
        print("\n--- Arama Sonuçları ---")
        for book in results:
            book.display_info()

    def save_to_json(self, filename="library_data.json"):
        data = []
        for book in self.books:
            data.append({
                "title": book.title,
                "author": book.author,
                "is_borrowed": book.is_borrowed,
                "due_date": book.due_date.strftime('%d-%m-%Y') if book.due_date else None
            })
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Kütüphane verileri '{filename}' dosyasına kaydedildi.")

library = Library()
while True:
    print("\n--- Kütüphane Yönetim Sistemi ---")
    print("1: Kitap ekle")
    print("2: Kitapları görüntüle")
    print("3: Kitap ödünç al")
    print("4: Kitap iade et")
    print("5: Kitap ara")
    print("6: Çıkış ve verileri kaydet")
    choice = input("Seçiminiz : ").strip()
    
    if choice == "1":
        title = input("Kitap başlığı: ").strip()
        author = input("Yazar: ").strip()
        library.add_book(title, author)
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        title = input("Ödünç almak istediğiniz kitap başlığı: ").strip()
        library.borrow_book(title)
    elif choice == "4":
        title = input("İade etmek istediğiniz kitap başlığı: ").strip()
        library.return_book(title)
    elif choice == "5":
        keyword = input("Aramak istediğiniz kelime: ").strip()
        library.search_book(keyword)
    elif choice == "6":
        library.save_to_json()
        print("Programdan çıkılıyor.")
        break
    else:
        print("Geçersiz seçim. Tekrar deneyin.")
        

    
                        