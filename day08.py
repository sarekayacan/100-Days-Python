import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4)

def show_menu():
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phones = input("Enter phone numbers (comma separated): ").split(",")
    emails = input("Enter emails (comma separated): ").split(",")

    contacts[name] = {
        "phones": [p.strip() for p in phones if p.strip()],
        "emails": [e.strip() for e in emails if e.strip()]
    }

    print(f"{name} added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("Contact book is empty.")
        return

    for name, info in contacts.items():
        print(f"\nName: {name}")
        print("Phones:", ", ".join(info["phones"]))
        print("Emails:", ", ".join(info["emails"]))

def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\nName: {name}")
        print("Phones:", ", ".join(info["phones"]))
        print("Emails:", ", ".join(info["emails"]))
    else:
        print("Contact not found.")

def edit_contact(contacts):
    name = input("Enter name to edit: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return

    phones = input("Enter new phone numbers (comma separated): ").split(",")
    emails = input("Enter new emails (comma separated): ").split(",")

    contacts[name]["phones"] = [p.strip() for p in phones if p.strip()]
    contacts[name]["emails"] = [e.strip() for e in emails if e.strip()]

    print(f"{name} updated successfully.")

def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        show_menu()
        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            edit_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Contacts saved. Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

