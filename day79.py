#Language Translator Tool
import tkinter as tk
from deep_translator import GoogleTranslator

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    target_lang = target_lang_var.get()

    if not text:
        return

    translated = GoogleTranslator(source='auto', target=target_lang).translate(text)

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated)
    output_text.config(state="disabled")

root = tk.Tk()
root.title("Language Translator")
root.geometry("420x360")

tk.Label(root, text="Çevrilecek Metin").pack(pady=5)

input_text = tk.Text(root, height=6, width=45)
input_text.pack(pady=5)

tk.Label(root, text="Hedef Dil").pack(pady=5)

target_lang_var = tk.StringVar(root)
target_lang_var.set("es")

languages = {
    "İspanyolca": "es",
    "Fransızca": "fr",
    "Almanca": "de",
    "Türkçe": "tr",
    "İtalyanca": "it"
}

tk.OptionMenu(root, target_lang_var, *languages.values()).pack(pady=5)

tk.Button(root, text="ÇEVİR", command=translate_text).pack(pady=10)

tk.Label(root, text="Çeviri").pack(pady=5)

output_text = tk.Text(root, height=6, width=45, state="disabled")
output_text.pack(pady=5)

root.mainloop()
