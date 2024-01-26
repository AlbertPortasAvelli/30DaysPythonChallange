# quiz_app.py
from question_generator import generate_question
from score_tracker import ScoreTracker

def present_question(score_tracker):
    question, correct_answer = generate_question()
    user_answer = input(f"What is the answer to {question}? ")

    if user_answer.isdigit() and int(user_answer) == correct_answer:
        print("Correct!\n")
        score_tracker.increase_score()
    else:
        print(f"Wrong! The correct answer is {correct_answer}.\n")

def main():
    print("Welcome to the Quiz App!\n")

    num_questions = 5
    score_tracker = ScoreTracker()

    for _ in range(num_questions):
        present_question(score_tracker)

    final_score = score_tracker.get_score()
    print(f"Quiz completed! Your final score is: {final_score}")

if __name__ == "__main__":
    main()
