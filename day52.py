#File Organizer Tool
import os
import shutil #dosya taşıma işlemi

#Varsayılan dosya türleri
DEFAULT_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".xls"],
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac"]
}

#Klasörleri oluşturan fonksiyon
def create_folders(base_path, categories):
    for folder in list(categories.keys()) + ["Others"]:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

#Dosyanın hangi klasöre ait olduğunu bulan fonksiyon
def get_target_folder(file_name, categories):
    for folder, extensions in categories.items():
        if any(file_name.lower().endswith(ext) for ext in extensions):
            return folder
    return "Others"

#Dosyayı taşıyan fonksiyon
def move_file(file_path, base_path, folder_name, dry_run):
    target_folder = os.path.join(base_path, folder_name)
    if dry_run:
        print(f"[DRY RUN] {os.path.basename(file_path)} → {folder_name}")
    else:
        shutil.move(file_path, target_folder)

#Dosyaları organize eden fonksiyon
def organize_files(base_path, categories, dry_run=False):
    for file_name in os.listdir(base_path):
        file_path = os.path.join(base_path, file_name)

        if os.path.isfile(file_path):
            folder = get_target_folder(file_name, categories)
            move_file(file_path, base_path, folder, dry_run)

#Kullanıcıdan özel kategori alma
def get_custom_categories():
    categories = DEFAULT_CATEGORIES.copy()

    choice = input("Özel kategori eklemek ister misiniz? (e/h): ").lower()
    while choice == "e":
        folder = input("Klasör adı: ")
        exts = input("Uzantılar (.py,.java gibi): ")
        categories[folder] = [ext.strip() for ext in exts.split(",")]

        choice = input("Başka kategori eklemek ister misiniz? (e/h): ").lower()

    return categories

#Ana menü
def main():
    print("Dosya Düzenleyici Araca Hoş Geldiniz")

    base_path = input("Düzenlenecek klasör yolunu girin: ")

    if not os.path.exists(base_path):
        print("Geçersiz yol!")
        return

    categories = get_custom_categories()

    dry_run_choice = input("Dry Run (önizleme) yapılsın mı? (e/h): ").lower()
    dry_run = dry_run_choice == "e"

    create_folders(base_path, categories)
    organize_files(base_path, categories, dry_run)

    if dry_run:
        print("\nDry Run tamamlandı. Dosyalar taşınmadı.")
    else:
        print("\Dosyalar başarıyla düzenlendi!")

if __name__ == "__main__":
    main()
