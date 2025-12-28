#Expense Tracker App
import tkinter as tk
from tkinter import messagebox #Hata, uyarı, onay pencereleri göstermek için
import csv
import os #Dosya var mı yok mu diye kontrol etmek için
from datetime import datetime

FILE_NAME = "expenses.csv"
expenses = [] #Tüm harcamalar RAM’de burada tutulur

def load_expenses(): #Önceden kaydedilen harcamaları yükler
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, newline="", encoding="utf-8") as file: #Türkçe karakter bozulmasın diye utf-8
            reader = csv.reader(file)
            for row in reader: #CSV’deki her satırı sırayla al
                expenses.append(row)
                listbox.insert(tk.END, f"{row[0]} | {row[1]} TL | {row[2]} | {row[3]}")
        calculate_total()

def save_expenses(): #RAM’deki harcamaları CSV’ye yazan fonksiyon
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(expenses) #RAM’deki tüm harcamaları dosyaya yaz

def add_expense():
    category = category_var.get() #Dropdown’dan seçilen kategoriyi al
    amount = amount_entry.get() #Kullanıcının yazdığı tutarı al (string)
    desc = desc_entry.get() #Açıklamayı al

    if not amount.isdigit() or category == "Kategori Seç" or desc == "":
        messagebox.showerror("Hata", "Geçerli bilgiler gir")
        return

    date = datetime.now().strftime("%d-%m-%Y")
    expense = [date, category, amount, desc]
    expenses.append(expense)

    listbox.insert(tk.END, f"{date} | {category} | {amount} TL | {desc}")
    save_expenses()
    calculate_total()
    clear_inputs()

def delete_expense():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Hata", "Silmek için seçim yap")
        return

    index = selected[0] #Seçilen satırın index’i
    listbox.delete(index) #Ekrandan sil
    expenses.pop(index) #RAM’den de sil
    save_expenses()
    calculate_total()

def calculate_total():
    total = sum(float(exp[2]) for exp in expenses)
    total_label.config(text=f"Toplam Harcama: {total:.2f} TL")

def clear_inputs():
    category_var.set("Kategori Seç")
    amount_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x550")

tk.Label(root, text="Expense Tracker", font=("Arial", 20, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

category_var = tk.StringVar(value="Kategori Seç")
tk.OptionMenu(frame, category_var, "Yemek", "Ulaşım", "Kira", "Fatura", "Diğer").grid(row=0, column=1)

tk.Label(frame, text="Kategori").grid(row=0, column=0)
tk.Label(frame, text="Tutar").grid(row=1, column=0)
tk.Label(frame, text="Açıklama").grid(row=2, column=0)

amount_entry = tk.Entry(frame)
amount_entry.grid(row=1, column=1)

desc_entry = tk.Entry(frame)
desc_entry.grid(row=2, column=1)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Ekle", command=add_expense).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Sil", command=delete_expense).grid(row=0, column=1, padx=5)

listbox = tk.Listbox(root, width=60, height=12)
listbox.pack(pady=10)

total_label = tk.Label(root, text="Toplam Harcama: 0 TL", font=("Arial", 12, "bold"))
total_label.pack(pady=5)

tk.Button(root, text="Çıkış", command=root.destroy).pack(pady=10)

load_expenses()
root.mainloop()
