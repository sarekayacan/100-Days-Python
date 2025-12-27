#Secure User Profile App
import json
import os
import re

DATA_FILE = "users.json"

class UserProfile:
    def __init__(self, username, email, password):
        self.username = username            # public
        self._email = email                 # protected
        self.__password = None              # private
        self.set_password(password)

    def set_password(self, new_password):
        if self.is_strong_password(new_password):
            self.__password = new_password
            print("Şifre başarıyla ayarlandı.")
        else:
            print("Zayıf şifre! (8 karakter, büyük/küçük harf, rakam)")

    def reset_password(self):
        new_password = input("Yeni şifreyi girin: ")
        self.set_password(new_password)

    def is_strong_password(self, password):
        if (len(password) >= 8 and
            re.search(r"[A-Z]", password) and
            re.search(r"[a-z]", password) and
            re.search(r"[0-9]", password)):
            return True
        return False

    def get_email(self):
        return self._email

    def set_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self._email = new_email
            print("E-posta güncellendi.")
        else:
            print("Geçersiz e-posta.")

    def display_profile(self):
        print("\n--- Kullanıcı Profili ---")
        print(f"Kullanıcı Adı: {self.username}")
        print(f"E-posta: {self._email}")
        print("Şifre: ********")

    def to_dict(self):
        return {
            "username": self.username,
            "email": self._email,
            "password": self.__password
        }

def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return [UserProfile(**u) for u in data]

def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump([u.to_dict() for u in users], f, indent=4)

users = load_users()

while True:
    print("\nSecure User Profile App")
    print("1. Kullanıcı oluştur")
    print("2. Profilleri görüntüle")
    print("3. E-posta güncelle")
    print("4. Şifre sıfırla")
    print("5. Çıkış")

    choice = input("Seçiminiz: ")

    if choice == "1":
        username = input("Kullanıcı adı: ")
        email = input("E-posta: ")
        password = input("Şifre: ")
        user = UserProfile(username, email, password)
        users.append(user)
        save_users(users)

    elif choice == "2":
        if not users:
            print("Kayıtlı kullanıcı yok.")
        for user in users:
            user.display_profile()

    elif choice == "3":
        username = input("Kullanıcı adı: ")
        for user in users:
            if user.username == username:
                new_email = input("Yeni e-posta: ")
                user.set_email(new_email)
                save_users(users)
                break
        else:
            print("Kullanıcı bulunamadı.")

    elif choice == "4":
        username = input("Kullanıcı adı: ")
        for user in users:
            if user.username == username:
                user.reset_password()
                save_users(users)
                break
        else:
            print("Kullanıcı bulunamadı.")

    elif choice == "5":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim.")
