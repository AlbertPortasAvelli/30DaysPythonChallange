### EXERCICES ###
# 1 - Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_to_wait = 18 - user_age
    print(f"You need {years_to_wait} more years to learn to drive.")
# 2 - Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences,
# and a custom text if my_age = your_age.
# Get user input for your age
your_age = int(input("Enter your age: "))
my_age = 30
if my_age < your_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print(f"You are {age_difference} year older than me.")
    else:
        print(f"You are {age_difference} years older than me.")
elif my_age > your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print(f"I am {age_difference} year older than you.")
    else:
        print(f"I am {age_difference} years older than you.")
else:
    print("We are the same age.")
# 3 - Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is smaller than {b}.")
else:
    print(f"{a} is equal to {b}.")

#============================================================================
# Level 2
#============================================================================

# 1 - Write a code which gives grade to students according to theirs scores:
#80-100, A
#70-89, B
#60-69, C
#50-59, D
#0-49, F
score = float(input("Enter the student's score: "))
if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score <= 89:
    grade = 'B'
elif 60 <= score <= 69:
    grade = 'C'
elif 50 <= score <= 59:
    grade = 'D'
elif 0 <= score <= 49:
    grade = 'F'
else:
    grade = 'Invalid input. Score must be between 0 and 100.'
print(f"The student's grade is: {grade}")
# 2 - Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter the name of the month: ").capitalize()
if month in ["September", "October", "November"]:
    season = "Autumn"
elif month in ["December", "January", "February"]:
    season = "Winter"
elif month in ["March", "April", "May"]:
    season = "Spring"
elif month in ["June", "July", "August"]:
    season = "Summer"
else:
    season = "Invalid input. Please enter a valid month."
print(f"The season in {month} is {season}.")
# 3 - The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()  # Convert to lowercase for case-insensitivity
if new_fruit in fruits:
    print(f'That fruit "{new_fruit}" already exists in the list.')
else:
    fruits.append(new_fruit)
    print(f'The modified list of fruits: {fruits}')

#=============================================================================
#Level 3
#=============================================================================

# 1 - Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
'''
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
'''if 'skills' in person:
    # Print the middle skill in the skills list
skills = person['skills']
if len(skills) > 0:
    middle_index = len(skills) // 2
    print(f"Middle skill in the skills list: {skills[middle_index]}")
    if 'Python' in skills:
        print("The person has 'Python' skill.")

    # Check for developer title based on skills
    if skills == ['JavaScript', 'React']:
        print("He is a front end developer")
    elif set(['Node', 'Python', 'MongoDB']).issubset(set(skills)):
        print("He is a backend developer")
    elif set(['React', 'Node', 'MongoDB']).issubset(set(skills)):
        print("He is a fullstack developer")
    else:
        print("Unknown title")
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} is married and lives in Finland.")