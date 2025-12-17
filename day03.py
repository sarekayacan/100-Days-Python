#Simple Calculator
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("\nChoose an operation:")
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("/ : Division")
print("** : Exponentiation (Power)")
print("% : Modulus (Remainder)")

operation = input("Enter your choice: ")

if operation == "+":
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")
    
elif operation == "-":
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nError: Division by zero is not allowed!")

elif operation == "**":
    result = num1 ** num2
    print(f"\nResult: {num1} ** {num2} = {result}")

elif operation == "%":
    result = num1 % num2
    print(f"\nResult: {num1} % {num2} = {result}")

else:
    print("\nInvalid operation selected!")
