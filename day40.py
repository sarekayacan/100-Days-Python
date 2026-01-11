#Triangle of Power
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

def guc_ucgeni_karsilastir(P, Q1, S1, Q2, S2):
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # 1 satır, 2 sütun

    # Başlangıç güç üçgeni
    A = (0, 0)
    B = (P, 0)
    C1 = (P, Q1)
    axs[0].plot([A[0], B[0]], [A[1], B[1]], label=f"P = {P:.2f} kW", color='orange')
    axs[0].plot([B[0], C1[0]], [B[1], C1[1]], label=f"Q = {Q1:.2f} kVAr", color='blue')
    axs[0].plot([A[0], C1[0]], [A[1], C1[1]], label=f"S = {S1:.2f} kVA", color='green')
    axs[0].set_title("Başlangıç Güç Üçgeni")
    axs[0].set_xlabel("Aktif Güç (kW)")
    axs[0].set_ylabel("Reaktif Güç (kVAr)")
    axs[0].axis("equal")
    axs[0].grid(True)
    axs[0].legend()

    # Düzeltilmiş güç üçgeni
    C2 = (P, Q2)
    axs[1].plot([A[0], B[0]], [A[1], B[1]], label=f"P = {P:.2f} kW", color='orange')
    axs[1].plot([B[0], C2[0]], [B[1], C2[1]], label=f"Q = {Q2:.2f} kVAr", color='blue')
    axs[1].plot([A[0], C2[0]], [A[1], C2[1]], label=f"S = {S2:.2f} kVA", color='green')
    axs[1].set_title("Düzeltilmiş Güç Üçgeni")
    axs[1].set_xlabel("Aktif Güç (kW)")
    axs[1].set_ylabel("Reaktif Güç (kVAr)")
    axs[1].axis("equal")
    axs[1].grid(True)
    axs[1].legend()

    plt.tight_layout()
    plt.show()

def hesapla():
    try:
        aktif = float(entry_aktif.get())
        cos_phi = float(entry_cosphi.get())
        new_cos_phi = float(entry_newcosphi.get())
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar giriniz!")
        return

    if not (0 < cos_phi <= 1) or not (0 < new_cos_phi <= 1):
        messagebox.showerror("Hata", "Güç faktörü 0 ile 1 arasında olmalıdır!")
        return

    # Başlangıç
    görünür = aktif / cos_phi
    reaktif = np.sqrt((görünür**2)-(aktif**2))

    # Düzeltilmiş
    new_görünür = aktif / new_cos_phi
    new_reaktif = np.sqrt((new_görünür**2)-(aktif**2))

    kondansatör = reaktif - new_reaktif

    sonuc.set(
        f"Başlangıç Görünür Güç: {görünür:.2f} kVA\n"
        f"Başlangıç Reaktif Güç: {reaktif:.2f} kVAr\n"
        f"Düzeltilmiş Görünür Güç: {new_görünür:.2f} kVA\n"
        f"Düzeltilmiş Reaktif Güç: {new_reaktif:.2f} kVAr\n"
        f"Eklenmesi gereken kondansatör: {kondansatör:.2f} kVAr"
    )

    guc_ucgeni_karsilastir(P=aktif, Q1=reaktif, S1=görünür, Q2=new_reaktif, S2=new_görünür)

root = Tk()
root.title("Güç Üçgeni ve Kompanzasyon")

Label(root, text="Aktif Güç (kW):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_aktif = Entry(root)
entry_aktif.grid(row=0, column=1, padx=5, pady=5)

Label(root, text="Başlangıç cosφ:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_cosphi = Entry(root)
entry_cosphi.grid(row=1, column=1, padx=5, pady=5)

Label(root, text="Yeni cosφ:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_newcosphi = Entry(root)
entry_newcosphi.grid(row=2, column=1, padx=5, pady=5)

Button(root, text="Hesapla ve Grafikleri Göster", command=hesapla).grid(row=3, column=0, columnspan=2, pady=10)

sonuc = StringVar()
Label(root, textvariable=sonuc, justify="left").grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()