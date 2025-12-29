#Data Cleaner
import pandas as pd
import os

def load_data(file_path):
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Desteklenmeyen dosya formatı!")

        print("\nVeri başarıyla yüklendi")
        return df

    except Exception as e:
        print("Veri yüklenemedi:", e)
        return None

def handle_missing_values(df):
    print("\nBoş değerler:")
    print(df.isnull().sum())

    choice = input("\nBoş değerler için seçim yap (1=Sil, 2=Doldur): ")

    if choice == "1":
        df = df.dropna()
        print("Boş değerler silindi")

    elif choice == "2":
        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].fillna("Unknown")
            else:
                df[col] = df[col].fillna(df[col].mean())
        print("Boş değerler dolduruldu")

    return df

def remove_duplicates(df):
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]

    print(f"\nDuplicate silindi: {before - after}")
    return df

def rename_columns(df):
    print("\nMevcut kolonlar:", list(df.columns))
    choice = input("Kolon adlarını değiştirmek ister misin? (e/h): ")

    if choice.lower() == "e":
        new_names = {}
        for col in df.columns:
            new_name = input(f"{col} → ")
            if new_name.strip() != "":
                new_names[col] = new_name

        df = df.rename(columns=new_names)
        print("✏️ Kolon isimleri güncellendi")

    return df

def transform_data(df):
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].str.strip().str.title()

    print("Metin kolonları düzenlendi")
    return df

def save_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"\nTemiz veri kaydedildi → {output_path}")

def main():
    print("\n=== DATA CLEANER TOOL ===")

    file_path = input("CSV veya Excel dosya yolu: ")
    df = load_data(file_path)

    if df is None:
        return

    print("\nİlk 5 satır:")
    print(df.head())

    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = rename_columns(df)
    df = transform_data(df)

    output_path = input("\nKaydedilecek dosya adı (örn: clean_data.csv): ")
    save_data(df, output_path)

    print("\n🎉 Veri temizleme tamamlandı!")

if __name__ == "__main__":
    main()
