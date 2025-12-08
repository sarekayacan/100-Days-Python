# Welcome Message Generator
from datetime import datetime

name = input("What is your name? ").title()
surname = input("What is your surname? ").upper()
hobby = input("What is your favorite hobby? ").lower()
color = input("What is your favorite color? ").lower()

now = datetime.now()
date_time = now.strftime("%d.%m.%Y - %H:%M")

print("\n--- Welcome Message ---")
print(f"Date: {date_time}")
print(f"Hello, {name} {surname}")
print(f"Welcome to the world of Python programming.")
print(f"It is great to know that you love {hobby} and your favorite color is {color}.")