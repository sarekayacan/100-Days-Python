#To-Do List GUI
import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get() #Kullanıcının yazdığı metni alır
    priority = priority_var.get()

    if task.strip() == "":
        messagebox.showerror("Hata", "Görev boş olamaz")
        return

    task_listbox.insert(tk.END, f"[{priority}] {task}") #Görevi listenin en sonuna ekle
    task_entry.delete(0, tk.END)

def delete_task():
    selected = task_listbox.curselection() #curselection() : Kullanıcının listede hangi görevi seçtiğini söyler
    if selected:
        task_listbox.delete(selected[0]) #Seçilen görevi sil
    else:
        messagebox.showerror("Hata", "Silmek için görev seç")

def clear_tasks():
    task_listbox.delete(0, tk.END) #Listbox içindeki HER ŞEYİ SİL

def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as file: #Program kapanınca görevler kaybolmasın diye dosyaya yazılır
        for i in range(task_listbox.size()):
            file.write(task_listbox.get(i) + "\n")
    messagebox.showinfo("Bilgi", "Görevler kaydedildi")

root = tk.Tk()
root.title("To Do List")
root.geometry("400x500")

tk.Label(root, text="To Do List", font=("Arial", 20, "bold")).pack(pady=10)

task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=5)

priority_var = tk.StringVar(value="Normal")
tk.OptionMenu(root, priority_var, "Yüksek", "Normal", "Düşük").pack() #Göreve öncelik seçtirir

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Ekle", command=add_task).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Sil", command=delete_task).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Temizle", command=clear_tasks).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Kaydet", command=save_tasks).grid(row=0, column=3, padx=5)

frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(frame, width=45, height=15, yscrollcommand=scrollbar.set)
task_listbox.pack()

scrollbar.config(command=task_listbox.yview)

tk.Button(root, text="Çıkış", command=root.destroy).pack(pady=10)

root.mainloop()
