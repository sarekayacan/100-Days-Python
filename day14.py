#Random Password Generator
import random
import string

def generate_password(length=12, use_special=True):
    if length < 4:
        raise ValueError("Şifre uzunluğu en az 4 olmalıdır.")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation if use_special else ""

    all_characters = uppercase + lowercase + digits + special

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits)
    ]

    if use_special:
        password.append(random.choice(special))

    remaining_length = length - len(password)
    password += random.choices(all_characters, k=remaining_length)

    random.shuffle(password)
    return "".join(password)


def save_passwords(passwords):
    with open("passwords.txt", "a") as file:
        for pwd in passwords:
            file.write(pwd + "\n")


try:
    length = int(input("Şifre uzunluğunu girin (min 4): "))
    count = int(input("Kaç adet şifre üretmek istiyorsunuz?: "))

    special_choice = input("Özel karakterler dahil edilsin mi? (e/h): ").lower()
    use_special = special_choice == "e"

    passwords = []

    for i in range(count):
        pwd = generate_password(length, use_special)
        passwords.append(pwd)
        print(f"{i+1}. Şifre: {pwd}")

    save_choice = input("Şifreler dosyaya kaydedilsin mi? (e/h): ").lower()
    if save_choice == "e":
        save_passwords(passwords)
        print("Şifreler passwords.txt dosyasına kaydedildi.")

except ValueError as e:
    print("Hata:", e)
