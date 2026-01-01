#Mini Chatbot
import re

def get_response(user_input):
    user_input = user_input.lower()

    # Selamlaşma
    if re.search(r"\b(merhaba|selam|hi|hello)\b", user_input):
        return "Merhaba! Sana nasıl yardımcı olabilirim?"

    # Hal hatır sorma
    elif re.search(r"nasılsın|how are you", user_input):
        return "Ben bir chatbotum ama harikayım Sen nasılsın?"

    # İsim sorma
    elif re.search(r"(adın ne|ismin ne|your name)", user_input):
        return "Ben MiniChatbot Python ile yazıldım!"

    # Teşekkür
    elif re.search(r"(teşekkür|thanks|sağ ol)", user_input):
        return "Rica ederim! Yardımcı olabildiysem ne mutlu"

    # Olumsuz duygu
    elif re.search(r"(kötüyüm|üzgünüm|moralim bozuk)", user_input):
        return "Bunu duyduğuma üzüldüm, İstersen konuşabiliriz."

    # Veda
    elif re.search(r"(bye|görüşürüz|hoşçakal)", user_input):
        return "Görüşmek üzere! Kendine iyi bak."

    # Tanınmayan giriş
    else:
        return "Buna nasıl cevap vereceğimi bilmiyorum"


def chatbot():
    print("Merhaba! Ben bir chatbotum.")
    print("Sohbeti bitirmek için 'exit' yazabilirsin.\n")

    while True:
        user_input = input("Sen: ")

        # Çıkış kontrolü
        if "exit" in user_input.lower():
            print("Chatbot: Görüşürüz! Güzel bir gün dilerim")
            break

        # Cevap üret
        response = get_response(user_input)
        print("Chatbot:", response)


# Programın başlangıç noktası
if __name__ == "__main__":
    chatbot()
