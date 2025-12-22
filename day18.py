#To Do App
import json
import os

TASK_FILE = "tasks.json"
COMPLETED_FILE = "completed_tasks.json"

def ensure_file_exists(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump([], file, indent=2)


ensure_file_exists(TASK_FILE)
ensure_file_exists(COMPLETED_FILE)

def load_tasks():
    with open(TASK_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def save_completed_task(task):
    completed = []
    if os.path.exists(COMPLETED_FILE):
        with open(COMPLETED_FILE, "r") as file:
            completed = json.load(file)

    completed.append(task)

    with open(COMPLETED_FILE, "w") as file:
        json.dump(completed, file, indent=2)

def add_task():
    title = input("Enter task name: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    tasks = load_tasks()
    tasks.append({
        "title": title,
        "due_date": due_date,
        "status": "incomplete"
    })

    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(filter_type="all"):
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("\n--- TODO LIST ---")
    for i, task in enumerate(tasks, start=1):
        if filter_type == "completed" and task["status"] != "complete":
            continue
        if filter_type == "incomplete" and task["status"] != "incomplete":
            continue

        print(f"{i}. {task['title']} | Due: {task['due_date']} | Status: {task['status']}")


def update_task_status():
    tasks = load_tasks()
    view_tasks()

    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_status = input("Enter new status (complete/incomplete): ").strip().lower()
            tasks[index]["status"] = new_status

            if new_status == "complete":
                save_completed_task(tasks[index])

            save_tasks(tasks)
            print("Task status updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    tasks = load_tasks()
    view_tasks()

    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def show_menu():
    print("\n--- MINI TODO APP ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Completed Tasks")
    print("4. View Incomplete Tasks")
    print("5. Update Task Status")
    print("6. Delete Task")
    print("7. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks("all")
        elif choice == "3":
            view_tasks("completed")
        elif choice == "4":
            view_tasks("incomplete")
        elif choice == "5":
            update_task_status()
        elif choice == "6":
            delete_task()
        elif choice == "7":
            print("Exiting Todo App. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
