#Bank Account Simulator
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []  #işlem geçmişi
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Yatırma: +{amount} TL")
            print(f"{amount} TL yatırıldı. Yeni bakiye: {self.balance} TL")
        else:
            print("Geçersiz miktar. Yatırma 0'dan büyük olmalı.")
            
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount 
            self.transactions.append(f"Çekme: -{amount} TL")
            print(f"{amount} TL çekildi. Yeni bakiye: {self.balance} TL")
        else :
            print("Geçersiz veya yetersiz bakiye ile çekim yapılamaz.")
    
    def show_details(self):
        print(f"--- Hesap Detayları ---")
        print(f"Hesap Sahibi: {self.account_holder}")
        print(f"Bakiye: {self.balance} TL")
        print("İşlem Geçmişi:")
        if self.transactions:
            for t in self.transactions:
                print("-", t)
        else:
            print("Henüz işlem yapılmadı.")
            
    def add_interest(self, rate_percent):
        interest = self.balance * rate_percent / 100
        self.balance += interest
        self.transactions.append(f"Faiz: +{interest:.2f} TL")
        print(f"{rate_percent}% faiz eklendi. Yeni bakiye: {self.balance:.2f} TL")

    def transfer(self, target_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            self.transactions.append(f"Transfer: -{amount} TL -> {target_account.account_holder}")
            target_account.transactions.append(f"Transfer: +{amount} TL <- {self.account_holder}")
            print(f"{amount} TL {target_account.account_holder} hesabına transfer edildi.")
        else:
            print("Transfer yapılamaz: Geçersiz miktar veya yetersiz bakiye.")

accounts = {}

def create_account():
    name = input("Hesap sahibinin adı: ").strip()
    initial = float(input("İlk yatırmak istediğiniz miktar: "))
    account = BankAccount(name, initial)
    accounts[name] = account
    print("Hesap başarıyla oluşturuldu!")

def access_account():
    name = input("Hesap sahibinin adı: ").strip()
    if name in accounts:
        account = accounts[name]
        while True:
            print("\n1: Para yatır")
            print("2: Para çek")
            print("3: Hesap detaylarını göster")
            print("4: Faiz ekle")
            print("5: Hesaplar arası transfer")
            print("6: Çıkış")
            choice = input("Seçiminiz: ").strip()

            if choice == "1":
                amount = float(input("Yatırmak istediğiniz miktar: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Çekmek istediğiniz miktar: "))
                account.withdraw(amount)
            elif choice == "3":
                account.show_details()
            elif choice == "4":
                rate = float(input("Faiz oranı (%): "))
                account.add_interest(rate)
            elif choice == "5":
                target_name = input("Transfer yapmak istediğiniz hesap: ").strip()
                if target_name in accounts:
                    target_acc = accounts[target_name]
                    amount = float(input("Transfer miktarı: "))
                    account.transfer(target_acc, amount)
                else:
                    print("Hedef hesap bulunamadı.")
            elif choice == "6":
                break
            else:
                print("Geçersiz seçim. Tekrar deneyin.")
    else:
        print("Hesap bulunamadı. Lütfen önce hesap oluşturun.")

def main_menu():
    while True:
        print("\n--- Banka Hesabı Simülatörü ---")
        print("1: Hesap oluştur")
        print("2: Hesaba eriş")
        print("3: Çıkış")
        choice = input("Seçiminiz: ").strip()
        if choice == "1":
            create_account()
        elif choice == "2":
            access_account()
        elif choice == "3":
            print("Programdan çıkılıyor. Hoşçakal!")
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")

main_menu()