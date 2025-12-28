#BMI Calculator
import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get().replace(",", ".").strip())
        height = float(height_entry.get().replace(",", ".").strip())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            status = "Zayıf"
            tip = "Biraz daha dengeli ve yeterli beslenmelisin."
        elif 18.5 < bmi < 25:
            status = "Normal"
            tip = "Gayet iyi, bu şekilde devam"
        elif 25 < bmi < 30:
            status = "Fazla Kilolu"
            tip = "Biraz hareket ve beslenme düzeni faydalı olur."
        else:
            status = "Obez"
            tip = "Bir uzmana danışman iyi olabilir."

        result_label.config(
            text=f"BMI: {bmi:.2f}\nDurum: {status}\nÖneri: {tip}"
        )

    except:
        messagebox.showerror(
            "Hata",
            "Lütfen geçerli sayılar gir."
        )

def reset():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("BMI Hesaplayıcı")
root.geometry("400x350")

tk.Label(root, text="BMI Hesaplayıcı", font=("Arial", 18, "bold")).pack(pady=15)

tk.Label(root, text="Kilo (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(root, text="Boy (metre):").pack()
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

tk.Button(root, text="BMI Hesapla", command=calculate_bmi).pack(pady=10)
tk.Button(root, text="Sıfırla", command=reset).pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=15)

root.mainloop()
