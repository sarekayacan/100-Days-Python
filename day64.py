#PDF Merger Tool
from PyPDF2 import PdfReader, PdfWriter
import os

def get_pdf_order():
    files = input("Birleştirilecek PDF dosyalarını sırayla gir (virgülle ayır): ")
    return [f.strip() for f in files.split(",")]

def validate_files(pdf_list):
    for pdf in pdf_list:
        if not os.path.exists(pdf):
            print(f"Hata: {pdf} dosyası bulunamadı.")
            return False
    return True

def get_page_range(pdf):
    choice = input(f"{pdf} için sayfa aralığı belirtmek ister misin? (e/h): ").lower()
    if choice != "e":
        return None

    start = int(input("Başlangıç sayfası (1’den başlar): ")) - 1
    end = int(input("Bitiş sayfası: "))
    return (start, end)

def is_blank_page(page):
    text = page.extract_text()
    return text is None or text.strip() == ""

def merge_pdfs(pdf_list, output_file):
    writer = PdfWriter()

    for pdf in pdf_list:
        reader = PdfReader(pdf)
        page_range = get_page_range(pdf)

        pages = reader.pages
        if page_range:
            pages = pages[page_range[0]:page_range[1]]

        for page in pages:
            if not is_blank_page(page):
                writer.add_page(page)

    with open(output_file, "wb") as f:
        writer.write(f)

    print(f"\nBirleştirilmiş PDF oluşturuldu: {output_file}")

def main():
    print("PDF Birleştirme Aracına Hoş Geldin\n")

    pdf_list = get_pdf_order()
    if not validate_files(pdf_list):
        return

    output_file = input("Oluşturulacak PDF dosya adı (ör: sonuc.pdf): ")
    merge_pdfs(pdf_list, output_file)

if __name__ == "__main__":
    main()
