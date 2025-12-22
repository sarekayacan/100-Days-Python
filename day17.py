#Student Report Generator 
import csv

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def process_student_data(input_file, output_file):
    students = []

    try:
        with open(input_file, "r") as infile:
            reader = csv.DictReader(infile)

            for row in reader:
                name = row["name"]
                math = int(row["math"])
                science = int(row["science"])
                english = int(row["english"])

                average = round((math + science + english) / 3, 2)
                grade = calculate_grade(average)

                students.append({
                    "name": name,
                    "math": math,
                    "science": science,
                    "english": english,
                    "average": average,
                    "grade": grade
                })

        # Top performer
        top_avg = max(student["average"] for student in students)
        for student in students:
            student["top_performer"] = "YES" if student["average"] == top_avg else "NO"

        with open(output_file, "w", newline="") as outfile:
            fieldnames = [
                "name", "math", "science", "english",
                "average", "grade", "top_performer"
            ]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)

        print("Student report generated successfully.")

    except FileNotFoundError:
        print("Input CSV file not found.")
    except KeyError:
        print("Invalid column names in CSV file.")
    except Exception as e:
        print("An error occurred:", e)


def search_student(input_file):
    name_to_search = input("Enter student name to search: ").lower()

    try:
        with open(input_file, "r") as file:
            reader = csv.DictReader(file)
            found = False

            for row in reader:
                if row["name"].lower() == name_to_search:
                    print("\n--- Student Found ---")
                    print("Name:", row["name"])
                    print("Math:", row["math"])
                    print("Science:", row["science"])
                    print("English:", row["english"])
                    found = True
                    break

            if not found:
                print("Student not found.")

    except FileNotFoundError:
        print("Student file not found.")


def show_menu():
    print("\n--- Student Report Generator ---")
    print("1. Generate report")
    print("2. Search student by name")
    print("3. Exit")


def main():
    input_file = "students.csv"
    output_file = "student_report.csv"

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            process_student_data(input_file, output_file)
        elif choice == "2":
            search_student(input_file)
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()
