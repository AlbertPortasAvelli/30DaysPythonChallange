# Exercises
# ==========================================================================
#   Level 1
# ==========================================================================
#   1. Write a python comment saying 'Day 2: 30 Days of python programming'
#       Day 2: 30 Days of python programming
#   2. Declare a first name variable and assign a value to it
first_name = 'Albert'
#   3. Declare a last name variable and assign a value to it
last_name = 'Portas'
#   4. Declare a full name variable and assign a value to it
full_name = first_name + ' ' + last_name
#   5. Declare a country variable and assign a value to it
country = 'Spain'
#   6. Declare a city variable and assign a value to it
city = 'Girona'
#   7. Declare an age variable and assign a value to it
age = 30
#   8. Declare a year variable and assign a value to it
from datetime import datetime
current_year = datetime.now().year
#   9. Declare a variable is_married and assign a value to it
is_married = False
#   10. Declare a variable is_true and assign a value to it
is_true = True
#   11. Declare a variable is_light_on and assign a value to it
is_light_on = False
#   12. Declare multiple variable on one line
item_name, quantity, price = "Widget", 10, 5.99
# ==========================================================================
#   Level 2
# ==========================================================================
#   1. Check the data type of all your variables using type() built-in function
variable_names = ['first_name', 'last_name', 'full_name', 'country', 'city',
                  'age', 'current_year', 'is_married', 'is_true', 'is_light_on',
                  'item_name', 'quantity', 'price']

variable_values = [first_name, last_name, full_name, country, city, age, current_year,
                   is_married, is_true, is_light_on, item_name, quantity, price]
for name, value in zip(variable_names, variable_values):
    exec(f"{name} = {repr(value)}")

for name in variable_names:
    print(f"Type of {name}:", type(eval(name)))
#   2. Using the len() built-in function, find the length of your first name
first_name_length = len(first_name)
print(first_name_length)
#   3. Compare the length of your first name and your last name
print("The first name is equal to the last name." if first_name == last_name else "The first name is not equal to the last name.")
print("The first name comes before the last name alphabetically." if first_name < last_name else ("The first name comes after the last name alphabetically." if first_name > last_name else "The first name and last name are the same."))
#   4. Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4
#       4.1 Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
#       4.2 Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one
#       4.3 Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
#       4.4 Divide num_one by num_two and assign the value to a variable division
division = num_one/num_two
#       4.5 Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
#       4.6 Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
#       4.7 Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
#   5. The radius of a circle is 30 meters.
radius = 30
#       5.1 Calculate the area of a circle and assign the value to a variable name of area_of_circle

import math
def area_calculation(radius) :
    area = math.pi * (radius **2)
    return area

area_of_circle = area_calculation(radius)
#       5.2 Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

def circum_calculation(radius):
    circum = 2 * math.pi * radius
    return circum

circum_of_circle = circum_calculation(radius)
#       5.3 Take radius as user input and calculate the area.
radius_user = float(input('Introduce radius and i will calculate the area and the circumference of your circle : '))
area_user = area_calculation(radius_user)
print('Area : {}'.format(area_user))
#   6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))