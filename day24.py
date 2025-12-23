#Employee Management System 
import json

FILE_NAME = "employees.json"

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print("\n--- Employee Details ---")
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Salary:", self.salary)
        print("Bonus:", self.calculate_bonus())

    def calculate_bonus(self):
        return self.salary * 0.10

    def to_dict(self):
        return {
            "type": "Employee",
            "name": self.name,
            "emp_id": self.emp_id,
            "salary": self.salary
        }

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print("Department:", self.department)

    def calculate_bonus(self):
        return self.salary * 0.20

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Manager"
        data["department"] = self.department
        return data

class Developer(Employee):
    def __init__(self, name, emp_id, salary, language):
        super().__init__(name, emp_id, salary)
        self.language = language

    def display_info(self):
        super().display_info()
        print("Programming Language:", self.language)

    def calculate_bonus(self):
        return self.salary * 0.15

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Developer"
        data["language"] = self.language
        return data

class Intern(Employee):
    def __init__(self, name, emp_id, stipend):
        super().__init__(name, emp_id, stipend)

    def calculate_bonus(self):
        return 0

    def to_dict(self):
        return {
            "type": "Intern",
            "name": self.name,
            "emp_id": self.emp_id,
            "salary": self.salary
        }

def save_to_json(employees):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([e.to_dict() for e in employees], f, indent=4)

def load_from_json():
    employees = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            for e in data:
                if e["type"] == "Manager":
                    employees.append(Manager(e["name"], e["emp_id"], e["salary"], e["department"]))
                elif e["type"] == "Developer":
                    employees.append(Developer(e["name"], e["emp_id"], e["salary"], e["language"]))
                elif e["type"] == "Intern":
                    employees.append(Intern(e["name"], e["emp_id"], e["salary"]))
                else:
                    employees.append(Employee(e["name"], e["emp_id"], e["salary"]))
    except FileNotFoundError:
        pass
    return employees

employees = load_from_json()

while True:
    print("\n=== Employee Management System ===")
    print("1. Add Employee")
    print("2. Show All Employees")
    print("3. Search by Employee ID")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        print("\n1-Employee  2-Manager  3-Developer  4-Intern")
        t = input("Type: ")

        name = input("Name: ")
        emp_id = input("Employee ID: ")

        if t == "4":
            stipend = float(input("Stipend: "))
            employees.append(Intern(name, emp_id, stipend))
        else:
            salary = float(input("Salary: "))

            if t == "2":
                dept = input("Department: ")
                employees.append(Manager(name, emp_id, salary, dept))
            elif t == "3":
                lang = input("Programming Language: ")
                employees.append(Developer(name, emp_id, salary, lang))
            else:
                employees.append(Employee(name, emp_id, salary))

        save_to_json(employees)
        print("Employee added successfully.")

    elif choice == "2":
        if not employees:
            print("No employees found.")
        for e in employees:
            e.display_info()

    elif choice == "3":
        search_id = input("Enter Employee ID: ")
        found = False
        for e in employees:
            if e.emp_id == search_id:
                e.display_info()
                found = True
                break
        if not found:
            print("Employee not found.")

    elif choice == "4":
        save_to_json(employees)
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
