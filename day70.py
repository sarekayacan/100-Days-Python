#Data Visualizer App
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

df = None
canvas = None

def load_file(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Desteklenmeyen dosya formatı")

def open_file():
    return filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")]
    )

def handle_file_upload():
    global df
    try:
        file_path = open_file()
        if not file_path:
            return
        df = load_file(file_path)
        update_dropdowns(df.columns)
        messagebox.showinfo("Başarılı", "Dosya yüklendi!")
    except Exception as e:
        messagebox.showerror("Hata", str(e))

def update_dropdowns(columns):
    x_menu['menu'].delete(0, 'end')
    y_menu['menu'].delete(0, 'end')

    for col in columns:
        x_menu['menu'].add_command(label=col, command=tk._setit(x_var, col))
        y_menu['menu'].add_command(label=col, command=tk._setit(y_var, col))

def plot_data():
    global canvas
    try:
        if df is None:
            raise ValueError("Önce dosya yükleyin")

        x_col = x_var.get()
        y_col = y_var.get()
        plot_type = plot_type_var.get()
        limit = int(row_limit.get())

        if not x_col or not y_col:
            raise ValueError("X ve Y eksenlerini seçin")

        data = df[[x_col, y_col]].head(limit)

        fig = Figure(figsize=(6,4))
        ax = fig.add_subplot(111)

        if plot_type == "Line":
            ax.plot(data[x_col], data[y_col])
        elif plot_type == "Bar":
            ax.bar(data[x_col], data[y_col])
        elif plot_type == "Scatter":
            ax.scatter(data[x_col], data[y_col])

        ax.set_title(f"{plot_type} Grafik")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)

        if canvas:
            canvas.get_tk_widget().destroy()

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)

    except Exception as e:
        messagebox.showerror("Hata", str(e))

def save_plot():
    if canvas is None:
        messagebox.showerror("Hata", "Önce grafik oluşturun")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Files", "*.png")]
    )
    if file_path:
        canvas.figure.savefig(file_path)
        messagebox.showinfo("Başarılı", "Grafik kaydedildi!")

root = tk.Tk()
root.title("Data Visualizer")
root.geometry("800x700")

tk.Button(root, text="Dosya Yükle", command=handle_file_upload).pack(pady=10)

x_var = tk.StringVar()
y_var = tk.StringVar()
plot_type_var = tk.StringVar(value="Line")
row_limit = tk.StringVar(value="10")

tk.Label(root, text="X Ekseni").pack()
x_menu = tk.OptionMenu(root, x_var, "")
x_menu.pack()

tk.Label(root, text="Y Ekseni").pack()
y_menu = tk.OptionMenu(root, y_var, "")
y_menu.pack()

tk.Label(root, text="Grafik Türü").pack()
tk.OptionMenu(root, plot_type_var, "Line", "Bar", "Scatter").pack()

tk.Label(root, text="Gösterilecek Satır Sayısı").pack()
tk.Entry(root, textvariable=row_limit).pack()

tk.Button(root, text="Grafik Oluştur", command=plot_data).pack(pady=10)
tk.Button(root, text="Grafiği Kaydet (PNG)", command=save_plot).pack()

root.mainloop()
