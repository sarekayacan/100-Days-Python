#Simple Login System
import tkinter as tk
from tkinter import messagebox

users = {
    "admin": "Admin123",
    "user": "User123"
}
attempts = 0
MAX_ATTEMPTS = 3

def password_strength(password):
    if len(password) < 6:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    return True

def login():
    global attempts

    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Hata", "Alanlar boş bırakılamaz")
        return

    if attempts >= MAX_ATTEMPTS:
        messagebox.showerror("Kilitlendi", "Çok fazla hatalı deneme!")
        return

    if username in users and users[username] == password:
        if not password_strength(password):
            messagebox.showwarning(
                "Zayıf Şifre",
                "Şifre en az 6 karakter, büyük harf ve rakam içermeli"
            )
            return

        messagebox.showinfo("Başarılı", f"Hoş geldin {username}")
        attempts = 0
    else:
        attempts += 1
        messagebox.showerror(
            "Hata",
            f"Yanlış giriş! Kalan deneme: {MAX_ATTEMPTS - attempts}"
        )

def clear_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Login System")
root.geometry("350x300")

tk.Label(root, text="Login System", font=("Arial", 18, "bold")).pack(pady=15)

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=10)
tk.Button(root, text="Clear", command=clear_fields).pack()
tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

root.mainloop()
