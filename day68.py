#Task Scheduler
import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_PATH = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

def update_task_list(filtered_tasks=None):
    task_listbox.delete(0, tk.END)
    display_tasks = filtered_tasks if filtered_tasks is not None else tasks

    for task in display_tasks:
        status = "✔" if task["completed"] else "✘"
        task_listbox.insert(
            tk.END,
            f"{status} [{task['priority']}] {task['title']} - {task['due_date']}"
        )

def add_task():
    title = title_entry.get()
    due_date = date_entry.get()
    priority = priority_var.get()

    if not title or not due_date:
        messagebox.showwarning("Hata", "Tüm alanları doldurun!")
        return

    tasks.append({
        "title": title,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    })

    save_tasks(tasks)
    update_task_list()

    title_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

def mark_completed():
    selection = task_listbox.curselection()
    if selection:
        tasks[selection[0]]["completed"] = True
        save_tasks(tasks)
        update_task_list()

def delete_task():
    selection = task_listbox.curselection()
    if selection:
        tasks.pop(selection[0])
        save_tasks(tasks)
        update_task_list()

def search_tasks():
    query = search_entry.get().lower()
    filtered = [t for t in tasks if query in t["title"].lower()]
    update_task_list(filtered)

root = tk.Tk()
root.title("Task Scheduler")
root.geometry("650x500")

# Title
tk.Label(root, text="Görev Adı").pack()
title_entry = tk.Entry(root, width=40)
title_entry.pack()

# Date
tk.Label(root, text="Son Tarih (YYYY-MM-DD)").pack()
date_entry = tk.Entry(root, width=40)
date_entry.pack()

# Priority
tk.Label(root, text="Öncelik").pack()
priority_var = tk.StringVar(value="Medium")
tk.OptionMenu(root, priority_var, "High", "Medium", "Low").pack()

# Add Button
tk.Button(root, text="Görev Ekle", command=add_task).pack(pady=5)

# Search
tk.Label(root, text="Görev Ara").pack()
search_entry = tk.Entry(root, width=40)
search_entry.pack()
tk.Button(root, text="Ara", command=search_tasks).pack(pady=5)

# Listbox
task_listbox = tk.Listbox(root, width=70, height=12)
task_listbox.pack(pady=10)

# Action Buttons
tk.Button(root, text="Tamamlandı Olarak İşaretle", command=mark_completed).pack(pady=3)
tk.Button(root, text="Görevi Sil", command=delete_task).pack(pady=3)

update_task_list()
root.mainloop()
