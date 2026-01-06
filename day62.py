#Automated Backup Tool
import os
import shutil
from datetime import datetime

#Dosyaları listeleme
def list_files(directory):
    return [
        f for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]

#Dosya kopyalama
def copy_file(source, destination):
    shutil.copy2(source, destination)

#Timestamp'li yedek klasörü oluşturma
def create_backup_directory(base_backup_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(base_backup_dir, f"backup_{timestamp}")
    os.makedirs(backup_dir, exist_ok=True)
    return backup_dir

#Yedekleme işlemi
def backup_files(source_dir, backup_dir):
    files = list_files(source_dir)
    for file in files:
        src = os.path.join(source_dir, file)
        dst = os.path.join(backup_dir, file)
        copy_file(src, dst)
        print(f"Yedeklendi: {file}")
    return files

#Log yazma
def write_log(backup_dir, log_file, files):
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"\nYedek oluşturuldu: {backup_dir}\n")
        for file in files:
            log.write(f"- {file}\n")

#ZIP oluşturma
def zip_backup(backup_dir):
    zip_path = shutil.make_archive(backup_dir, 'zip', backup_dir)
    print(f"ZIP oluşturuldu: {zip_path}")
    return zip_path

#Restore (geri yükleme)
def restore_backup(zip_file, restore_dir):
    shutil.unpack_archive(zip_file, restore_dir)
    print("Yedek geri yüklendi.")

#ANA PROGRAM
def main():
    print("Otomatik Yedekleme Aracı")

    source_dir = input("Kaynak klasör: ")
    base_backup_dir = input("Yedek klasör: ")
    log_file = input("Log dosyası (ör: log.txt): ")

    if not os.path.exists(source_dir):
        print("Kaynak klasör bulunamadı.")
        return

    os.makedirs(base_backup_dir, exist_ok=True)

    backup_dir = create_backup_directory(base_backup_dir)
    files = backup_files(source_dir, backup_dir)
    write_log(backup_dir, log_file, files)

    zip_path = zip_backup(backup_dir)

    print("Yedekleme tamamlandı.")
    print(f"Log: {log_file}")

    restore = input("Yedeği geri yüklemek ister misin? (e/h): ")
    if restore.lower() == "e":
        restore_dir = input("Geri yüklenecek klasör: ")
        os.makedirs(restore_dir, exist_ok=True)
        restore_backup(zip_path, restore_dir)

if __name__ == "__main__":
    main()
