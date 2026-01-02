#ASCII Art Generator
from PIL import Image
from colorama import Fore, Style, init

init(autoreset=True)

ASCII_CHARS = ["@", "%", "#", "*", "+", "=", "-", ":", ".", " "] #Koyu → açık sıralı karakterler

def load_image(image_path, new_width=100): #Oranı bozmadan yeniden boyutlandırır
    image = Image.open(image_path)
    aspect_ratio = image.height / image.width
    new_height = int(new_width * aspect_ratio * 0.55) #Karakterlerin dikey uzunluğu için düzeltme
    return image.resize((new_width, new_height))

def convert_to_grayscale(image):
    return image.convert("L") #Renkleri parlaklık değerine indirger (0–255)

def map_pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel // 25] for pixel in pixels)
    return ascii_str

def colorize_ascii(pixel_value, char): #Piksel parlaklığına göre renk verir
    if pixel_value < 50:
        return Fore.RED + char
    elif pixel_value < 100:
        return Fore.YELLOW + char
    elif pixel_value < 150:
        return Fore.GREEN + char
    elif pixel_value < 200:
        return Fore.CYAN + char
    else:
        return Fore.WHITE + char

def generate_ascii_art(image_path, new_width=100, colored=True):
    image = load_image(image_path, new_width)
    gray_image = convert_to_grayscale(image)
    pixels = gray_image.getdata()

    ascii_art = ""
    index = 0

    for pixel in pixels:
        char = ASCII_CHARS[pixel // 25]
        if colored:
            ascii_art += colorize_ascii(pixel, char)
        else:
            ascii_art += char
        index += 1
        if index % new_width == 0:
            ascii_art += "\n"

    return ascii_art

def save_ascii_art(ascii_art, output_path):
    with open(output_path, "w") as file:
        file.write(ascii_art)

def main():
    print("ASCII Art Generator'a Hoş Geldiniz!")

    image_path = input("Resim dosyasının yolunu girin: ")
    output_path = input("ASCII art kaydedilecek dosya adı (örnek: output.txt): ")
    width_input = input("ASCII art genişliği (varsayılan 100): ")

    width = int(width_input) if width_input.strip() else 100

    try:
        ascii_art = generate_ascii_art(image_path, width, colored=True)
        print(ascii_art)
        save_ascii_art(ascii_art, output_path)
        print(f"\nASCII art başarıyla oluşturuldu: {output_path}")
    except Exception as e:
        print("Hata oluştu:", e)

if __name__ == "__main__":
    main()
