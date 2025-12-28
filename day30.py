#Click Counter App
import tkinter as tk
import time
from tkinter import messagebox

#başlangıç zamanı
start_time = time.time()

counter = 0 #Kullanıcının mevcut tıklama sayısı
max_counter = 0 #Program çalıştığı sürece ulaşılan en yüksek değer

def update_labels():
    counter_label.config(text=f"Tıklama Sayısı: {counter}")
    max_label.config(text=f"En Yüksek Değer: {max_counter}")

def increment():
    global counter, max_counter
    counter += 1
    if counter > max_counter:
        max_counter = counter
    update_labels()
    #config(): Bir widget’ın özelliklerini canlı değiştirmeye yarar ve GUI’nin dinamik olmasını sağlar

def decrement():
    global counter
    if counter > 0:
        counter -= 1
    update_labels()

def reset_counter():
    global counter
    counter = 0
    update_labels()

def exit_app():
    elapsed_time = int(time.time() - start_time) #Toplam çalışma süresi (saniye)
    messagebox.showinfo(
        "Çıkış",
        f"Uygulama {elapsed_time} saniye çalıştı."
    )
    root.destroy()
    #GUI uygulamalarında destroy(): Belleği temizle ve programı düzgün kapatır

root = tk.Tk()
root.title("Click Counter App")
root.geometry("400x350")

tk.Label(
    root,
    text="Click Counter App",
    font=("Arial", 18, "bold")
).pack(pady=15)

counter_label = tk.Label(
    root,
    text="Tıklama Sayısı: 0",
    font=("Arial", 28)
)
counter_label.pack(pady=5)

max_label = tk.Label(
    root,
    text="En Yüksek Değer: 0",
    font=("Arial", 12)
)
max_label.pack(pady=5)

tk.Button(root, text="Artır", command=increment).pack(pady=5)
tk.Button(root, text="Azalt", command=decrement).pack(pady=5)
tk.Button(root, text="Sıfırla", command=reset_counter).pack(pady=5)
tk.Button(root, text="Çıkış", command=exit_app).pack(pady=15)

root.mainloop()
