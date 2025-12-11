#Math Quiz Game
import random
import time

def generate_question():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "*"])
    
    if operator == "+":
        answer = number1 + number2
    elif operator == "-":
        answer = number1 - number2
    else :
        answer = number1 * number2
    question_text = f"{number1} {operator} {number2} = ?"
    return question_text, answer

def math_quiz():
    question_number = int(input("Enter the number of questions you wish to answer: "))
    time_limit = float(input("Enter the time limit for answering the questions :"))
    
    score = 0
    for i in range(1, question_number+1):
        question_text, answer = generate_question()
        print(f"\nQuestion {i} : {question_text}")
        
        start_time = time.time()
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Counted as wrong.")
            continue
        
        elapsed = time.time() - start_time
        
        if elapsed > time_limit:
            print(f"Time's up! You took {elapsed:.2f} seconds.")
            print(f"Correct answer was: {answer}")
            continue
        
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {answer}")

    print("\n--- GAME OVER ---")
    print(f"Your final score: {score}/{question_number}")

    if score == question_number:
        print("Incredible! Perfect score!")
    elif score >= question_number // 2:
        print("Good job! You did well.")
    else:
        print("Keep practicing! You’ll get better.")

math_quiz()