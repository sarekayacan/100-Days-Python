#Sales Report Analyzer
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path): #Kullanıcının verdiği CSV dosyasını okur, hata varsa except bloğu yakalar, program patlamaz
    try:
        data = pd.read_csv(file_path)
        print("Veri başarıyla yüklendi")
        return data
    except Exception as e:
        print("Veri yüklenemedi:", e)
        return None

def clean_data(data): #Boş kategori varsa “Unknown” yapar
    print("\nVeri temizleniyor...")

    # Eksik kategori varsa doldur
    data["Product Category"] = data["Product Category"].fillna("Unknown")

    # Eksik satırları sil
    data = data.dropna()

    # Tarihi datetime yap
    data["Date"] = pd.to_datetime(data["Date"])

    # Sales Amount'u numeric yap
    data["Sales Amount"] = pd.to_numeric( #Bozuk veri varsa NaN yapar, programı kırmaz
        data["Sales Amount"], errors="coerce"
    )

    # Year-Month ekle
    data["Year_Month"] = data["Date"].dt.to_period("M")

    # Revenue hesapla
    if "Quantity" in data.columns and "Price" in data.columns:
        data["Revenue"] = data["Quantity"] * data["Price"]

    print("Veri temizlendi")
    return data

def analyze_data(data):
    print("\nSATIŞ İÇGÖRÜLERİ")

    monthly_sales = data.groupby("Year_Month")["Sales Amount"].sum()
    print("\nAylık Toplam Satışlar:")
    print(monthly_sales)

    # En çok kazandıran ürünler
    if "Revenue" in data.columns:
        top_products = (
            data.groupby("Product Name")["Revenue"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )

        print("\nEn Çok Kazandıran 5 Ürün:")
        print(top_products)

    return monthly_sales, top_products

def visualize(monthly_sales, data):
    # Bar chart
    monthly_sales.plot(
        kind="bar",
        figsize=(10, 6),
        title="Aylık Satışlar",
        ylabel="Toplam Satış",
        xlabel="Ay",
        color="skyblue"
    )
    plt.xticks(rotation=45)
    plt.show()

    # Pie chart (kategoriye göre)
    category_sales = data.groupby("Product Category")["Sales Amount"].sum()
    category_sales.plot(
        kind="pie",
        autopct="%1.1f%%",
        figsize=(7, 7),
        title="Kategoriye Göre Satış Dağılımı"
    )
    plt.ylabel("")
    plt.show()

def save_clean_data(data):
    choice = input("\nTemiz veriyi CSV olarak kaydetmek ister misin? (e/h): ")
    if choice.lower() == "e":
        filename = input("Dosya adı (örn: clean_sales.csv): ")
        data.to_csv(filename, index=False)
        print("Temiz veri kaydedildi")

def filter_by_category(data):
    choice = input("\nKategoriye göre filtrelemek ister misin? (e/h): ")
    if choice.lower() == "e":
        print("Mevcut kategoriler:", data["Product Category"].unique())
        category = input("Kategori seç: ")
        filtered = data[data["Product Category"] == category]
        print(filtered)
        return filtered
    return data

def main():
    print("=== SALES REPORT ANALYZER ===")

    file_path = input("CSV dosya yolunu gir: ")
    data = load_data(file_path)

    if data is None:
        return

    data = clean_data(data)
    data = filter_by_category(data)

    monthly_sales, _ = analyze_data(data)
    visualize(monthly_sales, data)

    save_clean_data(data)

    print("\nAnaliz tamamlandı!")

if __name__ == "__main__":
    main()
