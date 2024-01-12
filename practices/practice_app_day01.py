def get_valid_age_input():
    while True:
        try:
            age_input = input('Enter your age: ')
            age = int(age_input)
            if age < 0:
                raise ValueError("Age cannot be negative.")
            return age
        except ValueError:
            print("Invalid input. Please enter a valid positive integer for age.")

def get_player_info():
    player_name = input('Welcome to the math exam test app, please type your name: ')

    while True:
        player_age_problem = input('Hello {}, can you tell me your age? (Y/N): '.format(player_name))
        player_age_problem_response_lower = player_age_problem.lower()

        if player_age_problem_response_lower in {'y', 'yes'}:
            player_age = get_valid_age_input()
            break
        elif player_age_problem_response_lower in {'n', 'no'}:
            player_age = 'Unknown'
            print("Okay, no problem. I understand some people don't like to talk about their age.")
            break
        else:
            print('Invalid input. Please enter Y or N.')

    player_region = input('Can you tell me your country so we can finish the test and start calculating, please? ')

    return {
        'name': player_name,
        'age': player_age,
        'region': player_region
    }

def get_player_answers(questions):
    player_answer_list = []

    for i in range(len(questions)):
        while True:
            try:
                if i == 3:
                    player_answer_set = set(map(int, input(questions[i]).split()))
                    player_answer_list.append(player_answer_set)
                    break
                else:
                    player_answer = int(input(questions[i]))
                    player_answer_list.append(player_answer)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    return tuple(player_answer_list)

def evaluate_answers(answer_sheet_tuple, player_answer_tuple):
    check_answer_list = [ans_sheet == player_ans for ans_sheet, player_ans in zip(answer_sheet_tuple, player_answer_tuple)]

    print("Answer Sheet:", answer_sheet_tuple)
    print("Player Answers:", player_answer_tuple)
    print("Check Answer List:", check_answer_list)

    correct_answer = sum(check_answer_list)
    wrong_answer = len(questions) - correct_answer

    print('Congrats {}! You finished the math test with {} correct answers and {} wrong answers. Keep up the good work!'.format(player_info['name'], correct_answer, wrong_answer))
    print('Score\n=======================\nName: {}\nAge: {}\nCountry: {}\nScore: {}'.format(player_info['name'], player_info['age'], player_info['region'], correct_answer))

# Start of the main code
player_info = get_player_info()

questions = [
    "What is 1 + 13?\n",
    "Multiply these numbers: 3 x 4\n",
    "Resolve this equation and type the value of j: 2j - 5 = 3\n",
    'Tell me the numbers that are multipliers of 2: [5, 6, 31, 28, 12]'
]

last_answer_set = {6, 28, 12}
answer_sheet_tuple = (14, 12, 4, last_answer_set)

player_answer_tuple = get_player_answers(questions)

evaluate_answers(answer_sheet_tuple, player_answer_tuple)
