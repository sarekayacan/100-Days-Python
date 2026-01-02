#Pomodoro Timer
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import platform
import os

WORK_TIME = 25 * 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 15 * 60

session_count = 0 #Hangi oturumda olduğumuzu takip eder
timer_running = False
remaining_seconds = 0

window = tk.Tk()
window.title("Pomodoro Timer")
window.geometry("350x400")

timer_label = tk.Label(window, text="25:00", font=("Arial", 40))
timer_label.pack(pady=20)

status_label = tk.Label(window, text="Hazır", font=("Arial", 18))
status_label.pack()

progress = ttk.Progressbar(window, length=250)
progress.pack(pady=15)

def log_session(text):
    with open("session_history.txt", "a", encoding="utf-8") as file:
        file.write(f"{datetime.now()} - {text}\n")
        
def play_sound():
    system = platform.system()
    if system == "Windows":
        import winsound
        winsound.Beep(1000, 500)
    elif system == "Darwin":  # macOS
        os.system('afplay /System/Library/Sounds/Glass.aiff')
    else:  # Linux
        print('\a')

def countdown(): #Her saniye çağrılır, label günceller, progress bar ilerler
    global remaining_seconds, timer_running

    if remaining_seconds > 0 and timer_running:
        minutes, seconds = divmod(remaining_seconds, 60)
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

        progress['value'] += 1
        remaining_seconds -= 1
        window.after(1000, countdown)
    else:
        timer_running = False
        play_sound()
        start_timer()

def start_timer():
    global session_count, remaining_seconds, timer_running

    if timer_running:
        return

    timer_running = True

    if session_count % 8 == 7: #4 çalışma sonrası uzun mola
        remaining_seconds = LONG_BREAK
        status_label.config(text="Uzun Mola", fg="blue")
        log_session("Uzun mola")
    elif session_count % 2 == 0: #Çalışma oturumu
        remaining_seconds = WORK_TIME
        status_label.config(text="Çalışma Zamanı", fg="green")
        log_session("Çalışma oturumu")
    else: #Kısa mola
        remaining_seconds = SHORT_BREAK
        status_label.config(text="Kısa Mola", fg="orange")
        log_session("Kısa mola")

    progress['maximum'] = remaining_seconds
    progress['value'] = 0
    #Oturumun yüzde kaçının bittiğini gösterir

    session_count += 1
    countdown()

def reset_timer():
    global session_count, timer_running

    timer_running = False
    session_count = 0
    timer_label.config(text="25:00")
    status_label.config(text="Hazır", fg="black")
    progress['value'] = 0

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

start_btn = tk.Button(button_frame, text="Başlat", font=("Arial", 14), command=start_timer)
start_btn.pack(side="left", padx=10)

reset_btn = tk.Button(button_frame, text="Reset", font=("Arial", 14), command=reset_timer)
reset_btn.pack(side="right", padx=10)

window.mainloop()
