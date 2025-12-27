#Inventory Management System
import csv
from datetime import datetime

class Inventory:
    total_items = 0
    LOW_STOCK_LIMIT = 5
    global products

    def __init__(self, product_name, price, quantity, expiry_date=None):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.expiry_date = expiry_date

        Inventory.total_items += quantity

    def show_product_details(self):
        print("\n--- Ürün Detayları ---")
        print(f"Ürün: {self.product_name}")
        print(f"Fiyat: {self.price} ₺")
        print(f"Stok: {self.quantity}")
        if self.expiry_date:
            print(f"Son Kullanma Tarihi: {self.expiry_date}")
        self.stock_alert()
        
    def sell_product(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            Inventory.total_items -= amount
            print(f"{amount} adet {self.product_name} satıldı.")
            self.stock_alert()
        else:
            print("Yetersiz stok!")

    def stock_alert(self):
        if self.quantity <= Inventory.LOW_STOCK_LIMIT:
            print("UYARI: Stok azaldı!")

    # STATIC METHOD
    @staticmethod
    def calculate_discount(price, discount_percentage):
        return price * (1 - discount_percentage / 100)

    # CLASS METHOD
    @classmethod
    def total_items_report(cls):
        print(f"\nToplam Stoktaki Ürün Sayısı: {cls.total_items}")

    # CSV EXPORT
    @staticmethod
    def export_to_csv(products):
        with open("inventory.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Ürün Adı", "Fiyat", "Stok", "Son Kullanma Tarihi"])
            for product in products:
                writer.writerow([
                    product.product_name,
                    product.price,
                    product.quantity,
                    product.expiry_date
                ])
        print("inventory.csv dosyası oluşturuldu.")
        
    products = []

def add_product():
    name = input("Ürün adı: ")
    price = float(input("Fiyat: "))
    quantity = int(input("Stok miktarı: "))

    perishable = input("Bozulabilir mi? (e/h): ").lower()
    expiry_date = None
    if perishable == "e":
        expiry_date = input("Son kullanma tarihi (YYYY-AA-GG): ")

    product = Inventory(name, price, quantity, expiry_date)
    products.append(product)
    print(f"{quantity} adet {name} eklendi.")


def view_products():
    if not products:
        print("Envanter boş.")
    else:
        for product in products:
            product.show_product_details()


def sell_product():
    name = input("Satılacak ürün adı: ")
    for product in products:
        if product.product_name == name:
            amount = int(input("Satılacak miktar: "))
            product.sell_product(amount)
            return
    print("Ürün bulunamadı.")


def calculate_discount():
    price = float(input("Fiyat: "))
    discount = float(input("İndirim yüzdesi: "))
    final_price = Inventory.calculate_discount(price, discount)
    print(f"İndirimli fiyat: {final_price:.2f} ₺")


while True:
    print("""
--- INVENTORY MANAGEMENT SYSTEM ---
1. Ürün Ekle
2. Ürünleri Görüntüle
3. Ürün Sat
4. İndirim Hesapla
5. Toplam Stok Raporu
6. CSV’ye Aktar
7. Çıkış
""")

    choice = input("Seçiminiz (1-7): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        sell_product()
    elif choice == "4":
        calculate_discount()
    elif choice == "5":
        Inventory.total_items_report()
    elif choice == "6":
        Inventory.export_to_csv(products)
    elif choice == "7":
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim!")
