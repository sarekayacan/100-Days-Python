#Expense Tracker
import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def log_expense(date, category, amount, description):
    with open("expenses.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

def load_expenses(): #CSV dosyasını pandas DataFrame olarak okur ve Kolon isimlerini manuel veriyoruz
    return pd.read_csv(
        "expenses.csv",
        names=["Date", "Category", "Amount", "Description"]
    )

def summarize_expenses(df): #groupby("Category") : kategoriye göre grupla
    summary = df.groupby("Category")["Amount"].sum()
    print("\nHarcama Özeti:")
    print(summary)
    return summary

def plot_expenses_by_category(df):
    summary = df.groupby("Category")["Amount"].sum()
    summary.plot(
        kind="pie",
        autopct="%1.1f%%",
        figsize=(8, 8),
        title="Harcama Dağılımı"
    )
    plt.ylabel("")
    plt.show()

def plot_monthly_trends(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    monthly = df.groupby("Month")["Amount"].sum()

    monthly.plot(kind="bar", figsize=(10, 6), title="Aylık Harcama Trendi")
    plt.xlabel("Ay")
    plt.ylabel("Toplam Harcama")
    plt.xticks(rotation=45)
    plt.show()

def delete_expense(index): #index’e göre silme işlemi yapar
    df = load_expenses()
    df.drop(index, inplace=True)
    df.to_csv("expenses.csv", index=False, header=False)
    print("Harcama silindi.")

def edit_expense(index, new_amount):
    df = load_expenses()
    df.at[index, "Amount"] = new_amount
    df.to_csv("expenses.csv", index=False, header=False)
    print("Harcama güncellendi.")

def export_to_excel():
    df = load_expenses()
    summary = df.groupby("Category")["Amount"].sum()
    summary.to_excel("expense_summary.xlsx")
    print("Excel dosyası oluşturuldu.")

def export_to_pdf():
    df = load_expenses()
    summary = df.groupby("Category")["Amount"].sum()

    pdf = SimpleDocTemplate("expense_summary.pdf")
    styles = getSampleStyleSheet()
    content = [Paragraph("Harcama Özeti", styles["Title"])]

    for cat, amt in summary.items():
        content.append(Paragraph(f"{cat}: {amt} ₺", styles["Normal"]))

    pdf.build(content)
    print("PDF dosyası oluşturuldu.")

def main():
    while True:
        print("""
1 - Harcama Ekle
2 - Harcama Özeti
3 - Grafik (Kategori)
4 - Grafik (Aylık)
5 - Harcama Sil
6 - Harcama Düzenle
7 - Excel'e Aktar
8 - PDF'e Aktar
9 - Çıkış
""")

        choice = input("Seçiminiz: ")

        if choice == "1":
            date = input("Tarih (YYYY-MM-DD): ")
            category = input("Kategori: ")
            amount = float(input("Tutar: "))
            desc = input("Açıklama: ")
            log_expense(date, category, amount, desc)

        elif choice == "2":
            summarize_expenses(load_expenses())

        elif choice == "3":
            plot_expenses_by_category(load_expenses())

        elif choice == "4":
            plot_monthly_trends(load_expenses())

        elif choice == "5":
            idx = int(input("Silinecek index: "))
            delete_expense(idx)

        elif choice == "6":
            idx = int(input("Düzenlenecek index: "))
            amt = float(input("Yeni tutar: "))
            edit_expense(idx, amt)

        elif choice == "7":
            export_to_excel()

        elif choice == "8":
            export_to_pdf()

        elif choice == "9":
            print("Görüşürüz!")
            break

        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
