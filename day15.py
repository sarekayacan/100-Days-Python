#Recipe Viewer
def load_recipes(file_path):
    recipes = {}

    try:
        with open(file_path, "r") as file:
            content = file.read()
            recipe_blocks = content.strip().split("\n\n")

            for recipe in recipe_blocks:
                lines = recipe.split("\n")

                if len(lines) >= 3:
                    name = lines[0].strip()
                    ingredients = lines[1].replace("Ingredients:", "").strip()
                    instructions = lines[2].replace("Instructions:", "").strip()

                    recipes[name] = {
                        "ingredients": ingredients,
                        "instructions": instructions
                    }

    except FileNotFoundError:
        print("Recipe file not found.")

    return recipes


def save_recipes(file_path, recipes):
    with open(file_path, "w") as file:
        for name, data in recipes.items():
            file.write(f"{name}\n")
            file.write(f"Ingredients: {data['ingredients']}\n")
            file.write(f"Instructions: {data['instructions']}\n\n")


def show_menu():
    print("\n--- Recipe Viewer Menu ---")
    print("1. View recipe by name")
    print("2. List all recipes")
    print("3. Search recipes by ingredient")
    print("4. Add a new recipe")
    print("5. Exit")


def view_recipe(recipes):
    name = input("Enter recipe name: ").strip()

    if name in recipes:
        print(f"\n{name}")
        print("Ingredients:", recipes[name]["ingredients"])
        print("Instructions:", recipes[name]["instructions"])
    else:
        print("Recipe not found.")


def search_by_ingredient(recipes):
    ingredient = input("Enter ingredient to search: ").lower()
    found = False

    for name, data in recipes.items():
        if ingredient in data["ingredients"].lower():
            print(f"- {name}")
            found = True

    if not found:
        print("No recipes found with that ingredient.")


def add_recipe(recipes):
    name = input("Enter new recipe name: ").strip()

    if name in recipes:
        print("Recipe already exists.")
        return

    ingredients = input("Enter ingredients (comma separated): ").strip()
    instructions = input("Enter instructions: ").strip()

    recipes[name] = {
        "ingredients": ingredients,
        "instructions": instructions
    }

    print("Recipe added successfully!")


def main():
    file_path = "recipes.txt"
    recipes = load_recipes(file_path)

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_recipe(recipes)

        elif choice == "2":
            print("\nAvailable Recipes:")
            for name in recipes:
                print("-", name)

        elif choice == "3":
            search_by_ingredient(recipes)

        elif choice == "4":
            add_recipe(recipes)
            save_recipes(file_path, recipes)

        elif choice == "5":
            save_recipes(file_path, recipes)
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
