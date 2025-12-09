# Kişisel Selamlama Programı
name = input("What is your name? ")
last_name = input("What is your surname? ")
birth_year = int(input("What is your birth year "))
favorite_color = input("What is your favorite color? ")
current_year = 2025
age = current_year - birth_year

age_in_months = age * 12
age_in_weeks = age * 52
age_in_days = age * 365

nickname = name[:3] + "_python"
print("\n--Welcome to the personal greeting program--")
print(f"Hello! {name} {last_name}")
print(f"You are {age} years old")
print(f"- You are {age_in_months} months old")
print(f"- You are {age_in_weeks} weeks old")
print(f"- You are {age_in_days} days old")
print(f"Your favorite color is {favorite_color}")
print(f"Your nickname is {nickname}")

