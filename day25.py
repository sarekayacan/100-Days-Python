import random

class Animal:
    def make_sound(self):
        print("Bir hayvan sesi...")

class Dog(Animal):
    def make_sound(self):
        print("Woof Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow Meow!")

class Cow(Animal):
    def make_sound(self):
        print("Moo Moo!")

class Duck(Animal):
    def make_sound(self):
        print("Quack Quack!")

class AnimalSoundSimulator:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.__class__.__name__} simülatöre eklendi.")
        else:
            print("Geçersiz hayvan türü!")

    def remove_animal(self):
        if not self.animals:
            print("Silinecek hayvan yok.")
            return
        removed = self.animals.pop()
        print(f"{removed.__class__.__name__} simülatörden silindi.")

    def make_all_sounds(self):
        if not self.animals:
            print("Simülatörde hayvan yok.")
            return
        print("\nHayvan Sesleri:")
        for animal in self.animals:
            animal.make_sound()

    def animal_count(self):
        print(f"Toplam hayvan sayısı: {len(self.animals)}")

    def random_sound(self):
        if not self.animals:
            print("Simülatörde hayvan yok.")
            return
        animal = random.choice(self.animals)
        print("Rastgele Hayvan Sesi:")
        animal.make_sound()

simulator = AnimalSoundSimulator()

while True:
    print("\n--- Animal Sound Simulator ---")
    print("1. Köpek ekle")
    print("2. Kedi ekle")
    print("3. İnek ekle")
    print("4. Ördek ekle")
    print("5. Tüm sesleri çal")
    print("6. Hayvan sil")
    print("7. Hayvan sayısını göster")
    print("8. Rastgele hayvan sesi")
    print("9. Çıkış")

    choice = input("Seçiminizi girin: ")

    if choice == "1":
        simulator.add_animal(Dog())
    elif choice == "2":
        simulator.add_animal(Cat())
    elif choice == "3":
        simulator.add_animal(Cow())
    elif choice == "4":
        simulator.add_animal(Duck())
    elif choice == "5":
        simulator.make_all_sounds()
    elif choice == "6":
        simulator.remove_animal()
    elif choice == "7":
        simulator.animal_count()
    elif choice == "8":
        simulator.random_sound()
    elif choice == "9":
        print("Simülatörden çıkılıyor...")
        break
    else:
        print("Geçersiz seçim, tekrar deneyin.")
