#Ingredient Checker
recipes = {
    "Cake": {"flour", "sugar", "butter", "eggs", "milk"},
    "Pancake": {"flour", "milk", "eggs", "sugar"},
    "Omelette": {"eggs", "milk", "butter"}
}
alternatives = {
    "milk": {"almond milk", "soy milk"},
    "butter": {"margarine"},
    "sugar": {"honey"}
}

user_input = input(
    "Sahip olduğunuz malzemeleri virgülle ayırarak girin: ")

user_ingredients = set(
    ingredient.strip().lower()
    for ingredient in user_input.split(",")
)

print("\n--- MALZEME KONTROLÜ ---")

def check_recipe(recipe_name, recipe_ingredients):
    missing = recipe_ingredients - user_ingredients
    extra = user_ingredients - recipe_ingredients

    print(f"\nTarif: {recipe_name}")

    if not missing:
        print("Bu tarifi yapabilirsin!")
    else:
        print("Eksik malzemeler:", ", ".join(missing))

        # Alternatif kontrolü
        for item in missing:
            if item in alternatives:
                possible = alternatives[item] & user_ingredients
                if possible:
                    print(f"{item} yerine kullanabileceğin alternatif:",", ".join(possible))

    if extra:
        print("Fazla malzemeler:", ", ".join(extra))

print("\n--- TARİF ÖNERİLERİ ---")

available_recipes = []

for name, ingredients in recipes.items():
    if ingredients.issubset(user_ingredients):
        available_recipes.append(name)

if available_recipes:
    print("Yapabileceğin tarifler:")
    for r in available_recipes:
        print("-", r)
else:
    print("Şu an tam yapabileceğin bir tarif yok.")

#Tüm tarifleri detaylı kontrol et
for name, ingredients in recipes.items():
    check_recipe(name, ingredients)

#Tarifleri dosyaya kaydet
with open("recipes.txt", "w") as file:
    for name, ingredients in recipes.items():
        line = name + ":" + ",".join(ingredients) + "\n"
        file.write(line)

print("\nTarifler 'recipes.txt' dosyasına kaydedildi.")

print("\n--- DOSYADAN TARİFLER ---")

loaded_recipes = {}

with open("recipes.txt", "r") as file:
    for line in file:
        name, items = line.strip().split(":")
        loaded_recipes[name] = set(items.split(","))

for name, ingredients in loaded_recipes.items():
    print(name, "→", ingredients)
