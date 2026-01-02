#Music Playlist Organizer
import os
import shutil
import json
import hashlib
from mutagen import File
import tkinter as tk
from tkinter import filedialog, messagebox

def scan_directory(directory, extensions=(".mp3", ".flac", ".wav", ".ogg", ".aac")):
    music_files = []

    for root, _, files in os.walk(directory): #os.walk → klasör içini gezer
        for file in files:
            if file.lower().endswith(extensions): #endswith → sadece müzik dosyalarını alır
                music_files.append(os.path.join(root, file))

    return music_files

def extract_metadata(file_path):
    try:
        audio = File(file_path, easy=True) #easy=True → kolay erişilebilir tag’ler
        if audio is None:
            return None

        return {
            "title": audio.get("title", ["Unknown Title"])[0],
            "artist": audio.get("artist", ["Unknown Artist"])[0],
            "album": audio.get("album", ["Unknown Album"])[0],
            "genre": audio.get("genre", ["Unknown Genre"])[0],
            "path": file_path
        }
    except Exception as e:
        print(f"Hata: {file_path} → {e}")
        return None

def file_hash(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def organize_files(music_files, output_dir):
    seen_hashes = set()
    summary = []

    for file in music_files:
        metadata = extract_metadata(file)
        if not metadata:
            continue

        file_md5 = file_hash(file)
        if file_md5 in seen_hashes:
            print(f"Duplicate bulundu, atlandı: {file}")
            continue
        seen_hashes.add(file_md5)

        artist = metadata["artist"]
        album = metadata["album"]

        target_dir = os.path.join(output_dir, artist, album)
        os.makedirs(target_dir, exist_ok=True)

        destination = os.path.join(target_dir, os.path.basename(file))
        shutil.move(file, destination)

        metadata["new_path"] = destination
        summary.append(metadata)

    return summary

def save_summary(summary, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4, ensure_ascii=False)

def start_gui():
    def select_music_folder():
        path = filedialog.askdirectory()
        music_entry.delete(0, tk.END)
        music_entry.insert(0, path)

    def select_output_folder():
        path = filedialog.askdirectory()
        output_entry.delete(0, tk.END)
        output_entry.insert(0, path)

    def run_organizer():
        music_dir = music_entry.get()
        output_dir = output_entry.get()

        if not music_dir or not output_dir:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun")
            return

        files = scan_directory(music_dir)
        summary = organize_files(files, output_dir)
        save_summary(summary, "music_summary.json")

        messagebox.showinfo("Başarılı", "Müzikler başarıyla düzenlendi!")

    root = tk.Tk()
    root.title("Music Playlist Organizer")

    tk.Label(root, text="Müzik Klasörü").pack()
    music_entry = tk.Entry(root, width=50)
    music_entry.pack()
    tk.Button(root, text="Seç", command=select_music_folder).pack()

    tk.Label(root, text="Çıkış Klasörü").pack()
    output_entry = tk.Entry(root, width=50)
    output_entry.pack()
    tk.Button(root, text="Seç", command=select_output_folder).pack()

    tk.Button(root, text="Başlat", command=run_organizer, bg="green", fg="white").pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    start_gui()
