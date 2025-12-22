#Daily Journal Logger
from datetime import datetime

JOURNAL_FILE = "daily_journal.txt"


def add_entry():
    entry = input("Write your journal entry:\n").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(JOURNAL_FILE, "a") as file:
        file.write(f"[{timestamp}] {entry}\n")

    print("Entry added successfully.")


def view_entries():
    try:
        with open(JOURNAL_FILE, "r") as file:
            entries = file.readlines()

            if not entries:
                print("No entries found.")
                return

            print("\n--- Your Journal Entries ---")
            for i, entry in enumerate(entries, 1):
                print(f"{i}. {entry.strip()}")

    except FileNotFoundError:
        print("No journal file found. Add an entry first.")


def search_entries():
    keyword = input("Enter keyword to search: ").lower()

    try:
        with open(JOURNAL_FILE, "r") as file:
            entries = file.readlines()
            found = False

            print("\n--- Search Results ---")
            for entry in entries:
                if keyword in entry.lower():
                    print(entry.strip())
                    found = True

            if not found:
                print("No matching entries found.")

    except FileNotFoundError:
        print("No journal file found.")


def edit_entry():
    try:
        with open(JOURNAL_FILE, "r") as file:
            entries = file.readlines()

        view_entries()
        index = int(input("Enter entry number to edit: ")) - 1

        if 0 <= index < len(entries):
            new_text = input("Enter new text: ").strip()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            entries[index] = f"[{timestamp}] {new_text}\n"

            with open(JOURNAL_FILE, "w") as file:
                file.writelines(entries)

            print("Entry updated successfully.")
        else:
            print("Invalid entry number.")

    except (FileNotFoundError, ValueError):
        print("Error editing entry.")


def delete_entry():
    try:
        with open(JOURNAL_FILE, "r") as file:
            entries = file.readlines()

        view_entries()
        index = int(input("Enter entry number to delete: ")) - 1

        if 0 <= index < len(entries):
            entries.pop(index)

            with open(JOURNAL_FILE, "w") as file:
                file.writelines(entries)

            print("Entry deleted successfully.")
        else:
            print("Invalid entry number.")

    except (FileNotFoundError, ValueError):
        print("Error deleting entry.")


def export_journal():
    try:
        with open(JOURNAL_FILE, "r") as source:
            content = source.read()

        with open("journal_export.txt", "w") as export_file:
            export_file.write(content)

        print("Journal exported to journal_export.txt")

    except FileNotFoundError:
        print("No journal file to export.")


def show_menu():
    print("\n--- Daily Journal Logger ---")
    print("1. Add new entry")
    print("2. View all entries")
    print("3. Search entries by keyword")
    print("4. Edit an entry")
    print("5. Delete an entry")
    print("6. Export journal")
    print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            edit_entry()
        elif choice == "5":
            delete_entry()
        elif choice == "6":
            export_journal()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
