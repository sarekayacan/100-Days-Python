class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.__account_number = account_number
        self.__pin = pin
        self.__balance = balance
        self.transactions = [] #İşlem geçmişi listesi

    def validate_pin(self, entered_pin): #PIN’i göstermiyoruz, sadece kontrol ediyoruz.
        return entered_pin == self.__pin

    def check_balance(self):
        print(f"Mevcut bakiye: {self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append(f"{amount} TL yatırıldı")
            print(f"{amount} TL yatırıldı.")
        else:
            print("Geçersiz tutar.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Yetersiz bakiye!")
        elif amount > 0:
            self.__balance -= amount
            self.transactions.append(f"{amount} TL çekildi")
            print(f"{amount} TL çekildi.")
        else:
            print("Geçersiz tutar.")

    def change_pin(self, old_pin, new_pin):
        if self.validate_pin(old_pin) and len(new_pin) == 4 and new_pin.isdigit(): #Yeni PIN: 4 haneli ve Sadece rakam
            self.__pin = new_pin
            self.transactions.append("PIN değiştirildi")
            print("PIN başarıyla değiştirildi.")
        else:
            print("PIN değiştirilemedi.")

    def show_transactions(self):
        print("\nİşlem Geçmişi:")
        for t in self.transactions:
            print("-", t)

class SavingsAccount(BankAccount):
    def apply_interest(self):
        print("Faiz uygulandı (örnek).")

class ATM:
    ADMIN_PIN = "0000"

    def __init__(self):
        self.accounts = {}

    def create_account(self): #Yeni hesap yaratılır ve sözlüğe eklenir
        acc_no = input("Hesap numarası: ")
        pin = input("4 haneli PIN: ")

        if len(pin) == 4 and pin.isdigit():
            self.accounts[acc_no] = BankAccount(acc_no, pin)
            print("Hesap oluşturuldu.")
        else:
            print("Geçersiz PIN.")

    def authenticate(self):
        acc_no = input("Hesap numarası: ")
        pin = input("PIN: ")

        account = self.accounts.get(acc_no)
        if account and account.validate_pin(pin):
            self.account_menu(account)
        else:
            print("Hatalı giriş.")

    def admin_dashboard(self):
        pin = input("Admin PIN: ")
        if pin == ATM.ADMIN_PIN:
            print("\n--- ADMIN PANEL ---")
            print("Toplam hesap:", len(self.accounts))
        else:
            print("Yetkisiz giriş!")

    def account_menu(self, account):
        while True:
            print("""
1- Bakiye
2- Para yatır
3- Para çek
4- PIN değiştir
5- İşlem geçmişi
6- Çıkış
""")
            choice = input("Seçim: ")

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                account.deposit(int(input("Tutar: ")))
            elif choice == "3":
                account.withdraw(int(input("Tutar: ")))
            elif choice == "4":
                old = input("Eski PIN: ")
                new = input("Yeni PIN: ")
                account.change_pin(old, new)
            elif choice == "5":
                account.show_transactions()
            elif choice == "6":
                break
            else:
                print("Geçersiz seçim.")

    def main_menu(self):
        while True:
            print("""
--- MINI ATM ---
1- Hesap oluştur
2- Giriş yap
3- Admin panel
4- Çıkış
""")
            choice = input("Seçim: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.authenticate()
            elif choice == "3":
                self.admin_dashboard()
            elif choice == "4":
                print("Güle güle!")
                break
            else:
                print("Geçersiz seçim.")


if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()
