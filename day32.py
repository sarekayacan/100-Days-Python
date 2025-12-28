#Drawing Pad App
import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import ImageGrab

current_color = "black"
current_thickness = 2
actions = []        # Undo için çizilen objeler
redo_stack = []     # Redo için

def draw(event):
    x, y = event.x, event.y
    obj = canvas.create_oval(
        x - current_thickness,
        y - current_thickness,
        x + current_thickness,
        y + current_thickness,
        fill=current_color,
        outline=current_color
    )
    actions.append(obj)
    redo_stack.clear()

def undo():
    if actions:
        obj = actions.pop()
        canvas.delete(obj)
        redo_stack.append(obj)

def redo():
    if redo_stack:
        obj = redo_stack.pop()
        canvas.itemconfigure(obj, state="normal")
        actions.append(obj)

def clear_canvas():
    canvas.delete("all")
    actions.clear()
    redo_stack.clear()

def change_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color

def change_thickness(value):
    global current_thickness
    current_thickness = int(value)

def save_canvas():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Files", "*.png")]
    )
    if file_path:
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)

root = tk.Tk()
root.title("Drawing Pad (Bonuslu)")
root.geometry("650x650")

canvas = tk.Canvas(
    root,
    width=500,
    height=400,
    bg="white",
    bd=2,
    relief="ridge"
)
canvas.pack(pady=20)
canvas.bind("<B1-Motion>", draw)

control = tk.Frame(root)
control.pack()

tk.Button(control, text="Renk", command=change_color, width=8).grid(row=0, column=0, padx=5)
tk.Button(control, text="Undo", command=undo, width=8).grid(row=0, column=1, padx=5)
tk.Button(control, text="Redo", command=redo, width=8).grid(row=0, column=2, padx=5)
tk.Button(control, text="Temizle", command=clear_canvas, width=8).grid(row=0, column=3, padx=5)
tk.Button(control, text="Kaydet", command=save_canvas, width=8).grid(row=0, column=4, padx=5)

tk.Label(control, text="Kalınlık").grid(row=1, column=1, pady=10)

thickness_slider = tk.Scale(
    control,
    from_=1,
    to=10,
    orient="horizontal",
    command=change_thickness
)
thickness_slider.set(current_thickness)
thickness_slider.grid(row=1, column=2, columnspan=2)

root.mainloop()
