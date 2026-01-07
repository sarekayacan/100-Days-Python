#Currency Converter
import tkinter as tk
from tkinter import ttk
import requests

def load_rates_from_api():
    url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url, timeout=10)
    data = response.json()

    if data.get("result") != "success":
        raise Exception("Kur verisi alınamadı")

    return data["rates"]

def convert_currency(amount, from_cur, to_cur):
    usd_amount = amount / rates[from_cur]
    return usd_amount * rates[to_cur]

def handle_conversion():
    try:
        amount = float(amount_entry.get())
        from_cur = from_currency.get()
        to_cur = to_currency.get()

        result = convert_currency(amount, from_cur, to_cur)

        result_label.config(
            text=f"{amount} {from_cur} = {result:.2f} {to_cur}"
        )

    except ValueError:
        result_label.config(text="Geçerli bir sayı gir")
    except Exception:
        result_label.config(text="Dönüştürme hatası")

try:
    rates = load_rates_from_api()
except Exception:
    rates = {}
    print("API'den kur alınamadı")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("360x300")

currencies = list(rates.keys())

tk.Label(root, text="Miktar").pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Kaynak Para Birimi").pack()
from_currency = tk.StringVar(value="USD")
from_menu = ttk.Combobox(
    root, textvariable=from_currency, values=currencies, state="readonly"
)
from_menu.pack()

tk.Label(root, text="Hedef Para Birimi").pack()
to_currency = tk.StringVar(value="TRY")
to_menu = ttk.Combobox(
    root, textvariable=to_currency, values=currencies, state="readonly"
)
to_menu.pack()

tk.Button(root, text="Dönüştür", command=handle_conversion).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
