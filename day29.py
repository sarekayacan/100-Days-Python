#Simple GUI App
import tkinter as tk
from tkinter import StringVar

# ------------------ ANA PENCERE ------------------
root = tk.Tk()
root.title("Day 29 - Tkinter GUI")
root.geometry("400x350")

# ------------------ TEMALAR ------------------
LIGHT_BG = "#f0f0f0"
DARK_BG = "#2b2b2b"
LIGHT_TEXT = "#000000"
DARK_TEXT = "#ffffff"

current_theme = "light"

def apply_theme():
    bg = LIGHT_BG if current_theme == "light" else DARK_BG
    fg = LIGHT_TEXT if current_theme == "light" else DARK_TEXT

    root.config(bg=bg)
    for widget in root.winfo_children():
        try:
            widget.config(bg=bg, fg=fg)
        except:
            pass

# ------------------ TEMA DEĞİŞTİR ------------------
def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme()

# ------------------ ANİMASYONLU YAZI ------------------
def animate_text(text, index=0):
    if index <= len(text):
        greeting_label.config(text=text[:index])
        root.after(50, animate_text, text, index + 1)

# ------------------ SELAMLAMA ------------------
def greet_user():
    name = name_entry.get()
    lang = language.get()

    if not name:
        animate_text("Lütfen isminizi girin!")
        return

    greetings = {
        "Türkçe": f"Merhaba {name}",
        "English": f"Hello {name}",
        "Español": f"Hola {name}",
        "Deutsch": f"Hallo {name}"
    }

    animate_text(greetings.get(lang, f"Merhaba {name}"))

# ------------------ RESET ------------------
def reset():
    name_entry.delete(0, tk.END)
    greeting_label.config(text="")

# ------------------ BAŞLIK ------------------
title_label = tk.Label(root, text="Tkinter GUI Uygulaması", font=("Arial", 18))
title_label.pack(pady=15)

# ------------------ İSİM ------------------
tk.Label(root, text="İsminizi girin:").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# ------------------ DİL SEÇİMİ ------------------
tk.Label(root, text="Selamlama Dili:").pack()

language = StringVar(value="Türkçe")
language_menu = tk.OptionMenu(root, language, "Türkçe", "English", "Español", "Deutsch")
language_menu.pack(pady=5)

# ------------------ BUTONLAR ------------------
tk.Button(root, text="Greet Me", command=greet_user).pack(pady=5)
tk.Button(root, text="Reset", command=reset).pack(pady=5)
tk.Button(root, text="Tema Değiştir", command=toggle_theme).pack(pady=5)

# ------------------ SONUÇ ------------------
greeting_label = tk.Label(root, text="", font=("Arial", 14))
greeting_label.pack(pady=20)

apply_theme()
root.mainloop()
