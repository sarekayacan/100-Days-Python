#Personal Budget Planner
import tkinter as tk
from tkinter import messagebox
import csv
from collections import defaultdict
import matplotlib.pyplot as plt

users = {}

class User: #Her kullanıcı için ayrı bütçe tutar.
    def __init__(self, name):
        self.name = name
        self.goal = 0
        self.income = 0
        self.expenses = []

    def remaining_budget(self):
        total_expense = sum(exp["amount"] for exp in self.expenses)
        return self.income - total_expense #Toplam giderleri gelirden çıkarır

def export_to_csv(user): #Her kullanıcının giderlerini ayrı CSV’ye kaydeder
    filename = f"{user.name}_budget.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Amount"])
        for exp in user.expenses:
            writer.writerow([exp["category"], exp["amount"]])
    messagebox.showinfo("Başarılı", f"CSV kaydedildi: {filename}")

def plot_expenses(user):
    totals = defaultdict(float)
    for exp in user.expenses:
        totals[exp["category"]] += exp["amount"]

    plt.pie(totals.values(), labels=totals.keys(), autopct="%1.1f%%") #Giderleri kategori bazlı pasta grafiğiyle gösterir
    plt.title(f"{user.name} - Gider Dağılımı")
    plt.show()

def start_app():
    app = tk.Tk()
    app.title("Kişisel Bütçe Planlayıcı")

    tk.Label(app, text="Kullanıcı Adı").pack()
    name_entry = tk.Entry(app)
    name_entry.pack()

    def load_user():
        name = name_entry.get()
        if not name:
            messagebox.showerror("Hata", "İsim giriniz")
            return

        if name not in users:
            users[name] = User(name)

        user = users[name]

        def set_goal():
            user.goal = float(goal_entry.get())
            messagebox.showinfo("Başarılı", "Tasarruf hedefi ayarlandı")

        def set_income():
            user.income = float(income_entry.get())
            messagebox.showinfo("Başarılı", "Gelir eklendi")

        def add_expense():
            user.expenses.append({
                "category": category_entry.get().capitalize(),
                "amount": float(amount_entry.get())
            })
            messagebox.showinfo("Başarılı", "Gider eklendi")

        def check_goal():
            remaining = user.remaining_budget()
            if remaining >= user.goal:
                messagebox.showinfo("Tebrikler",
                    f"Hedefe ulaşıldı! Fazla: {remaining - user.goal:.2f}₺")
            else:
                messagebox.showwarning("Uyarı",
                    f"Hedefe {user.goal - remaining:.2f}₺ kaldı")

        tk.Label(app, text="Tasarruf Hedefi").pack()
        goal_entry = tk.Entry(app)
        goal_entry.pack()
        tk.Button(app, text="Hedef Ayarla", command=set_goal).pack()

        tk.Label(app, text="Gelir").pack()
        income_entry = tk.Entry(app)
        income_entry.pack()
        tk.Button(app, text="Gelir Ekle", command=set_income).pack()

        tk.Label(app, text="Gider Kategorisi").pack()
        category_entry = tk.Entry(app)
        category_entry.pack()

        tk.Label(app, text="Gider Tutarı").pack()
        amount_entry = tk.Entry(app)
        amount_entry.pack()
        tk.Button(app, text="Gider Ekle", command=add_expense).pack()

        tk.Button(app, text="Tasarruf Kontrol", command=check_goal).pack()
        tk.Button(app, text="Grafik Göster", command=lambda: plot_expenses(user)).pack()
        tk.Button(app, text="CSV'ye Aktar", command=lambda: export_to_csv(user)).pack()

    tk.Button(app, text="Kullanıcıyı Yükle", command=load_user).pack()
    app.mainloop()


start_app()
