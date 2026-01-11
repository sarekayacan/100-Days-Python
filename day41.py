#Electrical Analysis Tool
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

root = tk.Tk()
root.title("Elektrik Tüketim Analiz Aracı")
root.geometry("700x550")

def csv_yukle():
    dosya_yolu = filedialog.askopenfilename(
        title="CSV Dosyası Seç",
        filetypes=[("CSV dosyaları", "*.csv")]
    )
    if not dosya_yolu:
        return
    try:
        df = pd.read_csv(dosya_yolu)
        if not {'Tarih', 'Saat', 'Tuketim_kWh'}.issubset(df.columns):
            messagebox.showerror(
                "Hata",
                "CSV dosyası 'Tarih', 'Saat' ve 'Tuketim_kWh' sütunlarını içermelidir."
            )
            return
        df['TarihSaat'] = pd.to_datetime(
            df['Tarih'] + ' ' + df['Saat'].astype(str) + ':00'
        )
        toplam = df['Tuketim_kWh'].sum()
        lbl_toplam.config(text=f"Toplam Tüketim: {toplam:.2f} kWh")
        
        gunluk = df.groupby(df['Tarih'])['Tuketim_kWh'].sum()
        ort_gunluk = gunluk.mean()
        lbl_ortalama.config(text=f"Günlük Ortalama Tüketim: {ort_gunluk:.2f} kWh")

        max_idx = df['Tuketim_kWh'].idxmax()
        max_zaman = df.loc[max_idx, 'TarihSaat']
        max_tuketim = df.loc[max_idx, 'Tuketim_kWh']
        lbl_max.config(
            text=f"En Yüksek Tüketim: {max_tuketim:.2f} kWh ({max_zaman})"
        )
        fig.clear()
        ax = fig.add_subplot(111)

        ax.plot(
            df['TarihSaat'],
            df['Tuketim_kWh'],
            color='orange',
            marker='o',
            label='Gerçek Tüketim'
        )
        ax.set_title("Saatlik Tüketim ve Tahmin")
        ax.set_xlabel("Zaman")
        ax.set_ylabel("kWh")
        ax.tick_params(axis='x', rotation=45)

        df['Saat_num'] = np.arange(len(df))
        X = df[['Saat_num']]
        y = df['Tuketim_kWh']

        model = LinearRegression()
        model.fit(X, y)

        gelecek_saatler = pd.DataFrame({
            'Saat_num': np.arange(len(df), len(df) + 5)
        })
        tahminler = model.predict(gelecek_saatler)
        tahmin_zaman = pd.date_range(
            start=df['TarihSaat'].iloc[-1] + pd.Timedelta(hours=1),
            periods=5,
            freq='h'
        )
        ax.plot(
            tahmin_zaman,
            tahminler,
            color='red',
            marker='x',
            linestyle='--',
            label='Tahmin'
        )

        ax.legend()
        canvas.draw()

    except Exception as e:
        messagebox.showerror("Hata", f"Dosya okunamadı:\n{e}")

btn_yukle = tk.Button(root, text="CSV Yükle", command=csv_yukle)
btn_yukle.pack(pady=10)

lbl_toplam = tk.Label(root, text="Toplam Tüketim: -")
lbl_toplam.pack(pady=5)

lbl_ortalama = tk.Label(root, text="Günlük Ortalama Tüketim: -")
lbl_ortalama.pack(pady=5)

lbl_max = tk.Label(root, text="En Yüksek Tüketim: -")
lbl_max.pack(pady=5)

fig = plt.Figure(figsize=(6, 3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

root.mainloop()
