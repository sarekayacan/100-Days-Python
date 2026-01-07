#Stock Market Dashboard
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

def load_data(file_path="stock_data.csv"):
    return pd.read_csv(file_path, sep=";")

data = load_data()

COLUMN_MAP = {
    "stock": ["Stock", "Hisse", "Name"],
    "price": ["Price", "Fiyat"],
    "date": ["Date", "Tarih"]
}

def find_column(possible_names):
    for col in data.columns:
        if col.strip() in possible_names:
            return col
    return None

STOCK_COL = find_column(COLUMN_MAP["stock"])
PRICE_COL = find_column(COLUMN_MAP["price"])
DATE_COL = find_column(COLUMN_MAP["date"])

# Güvenlik kontrolü
if not all([STOCK_COL, PRICE_COL, DATE_COL]):
    raise ValueError("CSV dosyasında gerekli kolonlar bulunamadı.")

root = tk.Tk()
root.title("Stock Market Dashboard")
root.geometry("800x600")

current_canvas = None
current_figure = None

def plot_stock_data():
    global current_canvas, current_figure

    selected_stocks = stock_listbox.curselection()
    if not selected_stocks:
        messagebox.showwarning("Uyarı", "En az bir hisse seçmelisiniz.")
        return

    if current_canvas:
        current_canvas.get_tk_widget().destroy()

    fig = Figure(figsize=(7, 4), dpi=100)
    ax = fig.add_subplot(111)

    stats_text = ""

    for index in selected_stocks:
        stock_name = stock_listbox.get(index)
        filtered = data[data[STOCK_COL] == stock_name]

        ax.plot(
            filtered[DATE_COL],
            filtered[PRICE_COL],
            marker="o",
            label=stock_name
        )

        avg_price = filtered[PRICE_COL].mean()
        min_price = filtered[PRICE_COL].min()
        max_price = filtered[PRICE_COL].max()

        stats_text += (
            f"{stock_name} → Ortalama: {avg_price:.2f}, "
            f"Min: {min_price}, Max: {max_price}\n"
        )

    ax.set_title("Hisse Fiyat Trendleri")
    ax.set_xlabel("Tarih")
    ax.set_ylabel("Fiyat")
    ax.legend()
    ax.grid(True)

    stats_label.config(text=stats_text)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    current_canvas = canvas
    current_figure = fig

def save_plot():
    if current_figure is None:
        messagebox.showwarning("Uyarı", "Önce bir grafik çizmelisiniz.")
        return

    filename = f"stock_plot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    current_figure.savefig(filename)
    messagebox.showinfo("Kaydedildi", f"Grafik kaydedildi:\n{filename}")

title_label = tk.Label(root, text="Stock Market Dashboard", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

stock_label = tk.Label(root, text="Hisseleri Seç (Ctrl ile çoklu seçim):")
stock_label.pack()

stock_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=5)
for stock in data[STOCK_COL].unique():
    stock_listbox.insert(tk.END, stock)
stock_listbox.pack(pady=5)

plot_button = tk.Button(root, text="Grafiği Çiz", command=plot_stock_data)
plot_button.pack(pady=5)

save_button = tk.Button(root, text="Grafiği PNG Olarak Kaydet", command=save_plot)
save_button.pack(pady=5)

stats_label = tk.Label(root, text="", justify="left")
stats_label.pack(pady=10)

root.mainloop()
