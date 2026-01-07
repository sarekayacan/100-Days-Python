#Flashcards Learning App
import json
from datetime import datetime

FLASHCARDS_FILE = "flashcards.json"
LOG_FILE = "review_log.txt"

def load_flashcards():
    try:
        with open(FLASHCARDS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_flashcards(flashcards):
    with open(FLASHCARDS_FILE, "w", encoding="utf-8") as file:
        json.dump(flashcards, file, indent=4, ensure_ascii=False)

def log_review(question, user_answer, correct):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{time}] Soru: {question} | Cevap: {user_answer} | Doğru mu: {correct}\n")

def add_flashcard():
    question = input("Soru: ")
    answer = input("Cevap: ")
    category = input("Kategori (örn: Matematik, Tarih): ")

    flashcards = load_flashcards()
    flashcards.append({
        "question": question,
        "answer": answer,
        "category": category,
        "learned": False,
        "history": []
    })

    save_flashcards(flashcards)
    print("Flashcard eklendi!")

def review_flashcards():
    flashcards = load_flashcards()

    for card in flashcards:
        if not card["learned"]:
            print(f"\nKategori: {card['category']}")
            print("Soru:", card["question"])
            user_answer = input("Cevabınız: ")

            correct = user_answer.lower() == card["answer"].lower()
            card["history"].append({
                "answer": user_answer,
                "correct": correct
            })

            log_review(card["question"], user_answer, correct)

            if correct:
                print("Doğru!")
            else:
                print(f"Yanlış! Doğru cevap: {card['answer']}")

            save_flashcards(flashcards)
            return

    print("Gözden geçirilecek flashcard kalmadı.")


def mark_as_learned():
    flashcards = load_flashcards()

    for card in flashcards:
        if not card["learned"]:
            print("Soru:", card["question"])
            choice = input("Bu kart öğrenildi mi? (evet/hayır): ").lower()

            if choice == "evet":
                card["learned"] = True
                save_flashcards(flashcards)
                print("📘 Kart öğrenildi olarak işaretlendi.")
                return

    print("Tüm kartlar öğrenildi!")


def main():
    print("Flashcard Öğrenme Uygulamasına Hoş Geldiniz")

    while True:
        print("\n1. Flashcard ekle")
        print("2. Flashcard gözden geçir")
        print("3. Öğrenildi olarak işaretle")
        print("4. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            add_flashcard()
        elif choice == "2":
            review_flashcards()
        elif choice == "3":
            mark_as_learned()
        elif choice == "4":
            print("Güle güle!")
            break
        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    main()
