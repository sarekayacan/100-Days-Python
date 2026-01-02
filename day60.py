#Personal Diary App
import os
import shutil
from datetime import datetime
from cryptography.fernet import Fernet
import getpass
import tkinter as tk
from tkinter import messagebox, simpledialog

KEY_FILE = "secret.key"
ENTRIES_DIR = "entries"
BACKUP_DIR = "backup"

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)

def load_key():
    return open(KEY_FILE, "rb").read()

def encrypt_text(text):
    key = load_key()
    cipher = Fernet(key)
    return cipher.encrypt(text.encode())

def decrypt_text(encrypted_text):
    key = load_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_text).decode()

def authenticate():
    correct_password = "Diary@123"
    password = getpass.getpass("Şifreyi giriniz: ")
    return password == correct_password

def create_entry(title, content):
    os.makedirs(ENTRIES_DIR, exist_ok=True)
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    encrypted = encrypt_text(content)
    filename = f"{date}_{title}.txt"

    with open(os.path.join(ENTRIES_DIR, filename), "wb") as f:
        f.write(encrypted)

def list_entries():
    if not os.path.exists(ENTRIES_DIR):
        return []
    return os.listdir(ENTRIES_DIR)

def read_entry(filename):
    with open(os.path.join(ENTRIES_DIR, filename), "rb") as f:
        encrypted = f.read()
    return decrypt_text(encrypted)

def search_entries(keyword):
    results = []
    for entry in list_entries():
        content = read_entry(entry)
        if keyword.lower() in content.lower():
            results.append(entry)
    return results

def backup_entries():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    shutil.make_archive(
        os.path.join(BACKUP_DIR, "diary_backup"),
        'zip',
        ENTRIES_DIR
    )

def launch_gui(): #Grafik arayüzü başlatan fonksiyon
    root = tk.Tk() #Pencereyi oluşturma
    root.title("Kişisel Günlük")

    def new_entry(): #Yeni Günlük Ekleme
        title = simpledialog.askstring("Başlık", "Günlük başlığı:")
        content = simpledialog.askstring("İçerik", "Günlük içeriği:")
        if title and content:
            create_entry(title, content)
            messagebox.showinfo("Başarılı", "Günlük kaydedildi")

    def show_entries(): #Günlükleri Listeleme
        entries = list_entries()
        messagebox.showinfo("Günlükler", "\n".join(entries))

    def read_selected():
        filename = simpledialog.askstring("Oku", "Dosya adını gir:")
        try:
            content = read_entry(filename) #Hangi günlük okunacak sorulur
            messagebox.showinfo("İçerik", content)
        except:
            messagebox.showerror("Hata", "Dosya bulunamadı")

    def search():
        keyword = simpledialog.askstring("Ara", "Anahtar kelime:") #Kelime alınır
        results = search_entries(keyword) #Tüm günlükler içinde aranır
        messagebox.showinfo("Sonuçlar", "\n".join(results)) #Eşleşen dosyalar gösterilir

    def backup():
        backup_entries()
        messagebox.showinfo("Yedek", "Yedek alındı")

    tk.Button(root, text="Yeni Günlük", command=new_entry).pack()
    tk.Button(root, text="Günlükleri Listele", command=show_entries).pack()
    tk.Button(root, text="Günlük Oku", command=read_selected).pack()
    tk.Button(root, text="Ara", command=search).pack()
    tk.Button(root, text="Yedek Al", command=backup).pack()

    root.mainloop()

def main():
    generate_key()
    if authenticate():
        launch_gui()
    else:
        print("Erişim reddedildi")

if __name__ == "__main__":
    main()
