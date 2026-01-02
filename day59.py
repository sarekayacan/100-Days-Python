#Markdown to HTML Converter
import markdown
import os

def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def convert_markdown_to_html(markdown_text):
    return markdown.markdown(markdown_text)

def wrap_in_html_template(content, css_path=None):
    css_style = ""

    if css_path and os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as css_file:
            css_style = css_file.read()

    html_template = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>Markdown to HTML</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
            }}
            h1, h2, h3 {{
                color: #2c3e50;
            }}
            a {{
                color: #2980b9;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            {css_style}
        </style>
    </head>
    <body>
        {content}
    </body>
    </html>
    """
    return html_template

def write_html_file(html_content, output_path): #HTML çıktısı dosyaya yazılır
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)

def convert_folder(md_folder, output_folder, css_path=None): #Çıkış klasörü yoksa oluşturulur
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(md_folder): #Klasördeki tüm .md dosyaları bulunur
        if file_name.endswith(".md"):
            md_path = os.path.join(md_folder, file_name)
            html_path = os.path.join(
                output_folder,
                file_name.replace(".md", ".html")
            )
            md_text = read_markdown_file(md_path)
            html = convert_markdown_to_html(md_text)
            final_html = wrap_in_html_template(html, css_path)
            write_html_file(final_html, html_path)
            #Her dosya sırayla HTML’e çevrilir

def main():
    print("Markdown → HTML Dönüştürücü")
    mode = input("Tek dosya mı (1) yoksa klasör mü (2) dönüştürülecek? ")
    
    if mode == "1":
        md_path = input("Markdown dosya yolu: ")
        output_path = input("HTML çıkış yolu: ")
        css_path = input("CSS dosyası (boş bırakılabilir): ") or None
        md_text = read_markdown_file(md_path)
        html = convert_markdown_to_html(md_text)
        final_html = wrap_in_html_template(html, css_path)
        write_html_file(final_html, output_path)
        
    elif mode == "2":
        md_folder = input("Markdown klasörü yolu: ")
        output_folder = input("HTML çıkış klasörü: ")
        css_path = input("CSS dosyası (boş bırakılabilir): ") or None
        convert_folder(md_folder, output_folder, css_path)
        
    else:
        print("Geçersiz seçim!")
        
if __name__ == "__main__":
    main()
