# question_generator.py

import random

def generate_question():
    operators = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(operators)
    question = f"{num1} {operator} {num2}"
    answer = eval(question)  # Evaluate the expression to get the correct answer
    return question, answer
