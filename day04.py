def program():
    print("Number Comparison Tool")

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    number3 = float(input("Enter third number: "))

    print("\n--- Comparison Results ---")
    if number1 == number2 == number3:
        print(f"All numbers are equal: {number1}")
    else:
        largest = max(number1, number2, number3)
        print(f"The largest number is: {largest}")

    print("\n--- Number Analysis ---")
    def analyze(n):
        if n > 0:
            return "Positive"
        elif n < 0:
            return "Negative"
        else:
            return "Zero"

    print(f"{number1} is {analyze(number1)}")
    print(f"{number2} is {analyze(number2)}")
    print(f"{number3} is {analyze(number3)}")

    print("\nDo you want to restart the program?")
    choice = input("Type 'y' for yes or 'n' for no: ").lower()

    if choice == "y":
        program()
    else :
        print("Program ended.")
        
program()