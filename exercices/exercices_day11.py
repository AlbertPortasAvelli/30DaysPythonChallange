# Exercices

# 1 - Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    """This function takes two numbers as parameters and returns their sum."""
    result = num1 + num2
    return result
num1 = 5
num2 = 7
sum_result = add_two_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {sum_result}")
# 2 - Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
import math
def area_of_circle(radius):
    """This function calculates the area of a circle."""
    area = math.pi * radius ** 2
    return area
radius = 3.5
circle_area = area_of_circle(radius)
print(f"The area of a circle with radius {radius} is: {circle_area}")
# 3 - Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    """This function takes an arbitrary number of arguments, checks if they are numeric, and sums them."""
    total = 0

    for num in args:
        if not isinstance(num, (int, float)):
            print(f"Error: {num} is not a numeric type.")
            return None
        total += num

    return total
result1 = add_all_nums(1, 2, 3, 4)
result2 = add_all_nums(5, 6, "seven", 8)
print("Sum 1:", result1)
print("Sum 2:", result2)
# 4 - Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    """This function converts temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
temperature_celsius = 25
temperature_fahrenheit = convert_celsius_to_fahrenheit(temperature_celsius)
print(f"{temperature_celsius}°C is equal to {temperature_fahrenheit}°F")
# 5 - Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    """This function takes a month parameter and returns the season."""
    month = month.lower()

    if month in ["december", "january", "february"]:
        return "Winter"
    elif month in ["march", "april", "may"]:
        return "Spring"
    elif month in ["june", "july", "august"]:
        return "Summer"
    elif month in ["september", "october", "november"]:
        return "Autumn"
    else:
        return "Invalid month"
input_month = "June"
result_season = check_season(input_month)
print(f"The season for {input_month} is: {result_season}")
# 6 - Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    """This function calculates the slope of a linear equation."""
    try:
        slope = (y2 - y1) / (x2 - x1)
        return slope
    except ZeroDivisionError:
        print("Error: Division by zero. The slope is undefined for vertical lines.")
        return None
x1, y1 = 1, 3
x2, y2 = 5, 11
slope_result = calculate_slope(x1, y1, x2, y2)
if slope_result is not None:
    print(f"The slope of the line passing through ({x1}, {y1}) and ({x2}, {y2}) is: {slope_result}")
# 7 - Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import cmath  
def solve_quadratic_eqn(a, b, c):
    """This function calculates the solution set of a quadratic equation."""
    try:
        
        discriminant = cmath.sqrt(b**2 - 4*a*c)

        # Calculate the two solutions using the quadratic formula
        solution1 = (-b + discriminant) / (2*a)
        solution2 = (-b - discriminant) / (2*a)

        return solution1, solution2

    except ZeroDivisionError:
        print("Error: 'a' coefficient should not be zero.")
        return None
    except ValueError:
        print("Error: The discriminant is negative. The solutions involve complex numbers.")
        return None
a = 1
b = -3
c = 2
solutions = solve_quadratic_eqn(a, b, c)
if solutions is not None:
    print(f"The solutions of the quadratic equation {a}x² + {b}x + {c} = 0 are: {solutions}")
# 8 - Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(my_list):
    """This function prints out each element of the given list."""
    for element in my_list:
        print(element)
my_list = [1, 2, 3, 4, 5]
print_list(my_list)
'''
 9 - Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"] 
'''
def reverse_list(my_list):
    """This function returns the reverse of the given list using loops."""
    reversed_list = []
    for i in range(len(my_list) - 1, -1, -1):
        reversed_list.append(my_list[i])
    return reversed_list
example_list = [1, 2, 3, 4, 5]
reversed_result = reverse_list(example_list)
print(reversed_result)

def reverse_list_strings(my_list):
    """This function returns the reverse of the given list of strings using loops."""
    reversed_list = []
    for i in range(len(my_list) - 1, -1, -1):
        reversed_list.append(my_list[i])
    return reversed_list
example_list_strings = ["A", "B", "C"]
reversed_result_strings = reverse_list_strings(example_list_strings)
print(reversed_result_strings)
# 10 - Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(my_list):
    """This function returns a capitalized list of items."""
    capitalized_list = [item.capitalize() for item in my_list]
    return capitalized_list
example_list = ["apple", "banana", "cherry"]
capitalized_result = capitalize_list_items(example_list)
print(capitalized_result)
'''
 11 - Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
'''
def add_item(my_list, item):
    """This function returns a list with the item added at the end."""
    new_list = my_list.copy()
    new_list.append(item)
    return new_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
result_food = add_item(food_staff, 'Meat')
print(result_food)  

numbers = [2, 3, 7, 9]
result_numbers = add_item(numbers, 5)
print(result_numbers)  
'''
 12 - Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
'''
def remove_item(my_list, item):
    """This function returns a list with the specified item removed."""
    new_list = [element for element in my_list if element != item]
    return new_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
result_food = remove_item(food_staff, 'Mango')
print(result_food)  # Output: ['Potato', 'Tomato', 'Milk']

numbers = [2, 3, 7, 9]
result_numbers = remove_item(numbers, 3)
print(result_numbers)  # Output: [2, 7, 9]
'''
 13 - Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
'''
def sum_of_numbers(n):
    """This function adds all the numbers in the range from 1 to n."""
    return sum(range(1, n + 1))

print(sum_of_numbers(5))    
print(sum_of_numbers(10))   
print(sum_of_numbers(100))  
# 14 - Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    """This function adds all the odd numbers in the range from 1 to n."""
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

print(sum_of_odds(5))    
print(sum_of_odds(10))   
print(sum_of_odds(15))   
# 15 - Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    """This function adds all the even numbers in the range from 1 to n."""
    return sum(i for i in range(1, n + 1) if i % 2 == 0)

print(sum_of_even(5))    
print(sum_of_even(10))   
print(sum_of_even(15)) 

#=============================================================================
#Level 2
#=============================================================================

# 1 - Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(number):
    """This function counts the number of evens and odds in the given positive integer."""
    if number <= 0:
        return "Please provide a positive integer."

    evens_count = sum(1 for digit in str(number) if int(digit) % 2 == 0)
    odds_count = len(str(number)) - evens_count

    return f"The number of odds are {odds_count}.\nThe number of evens are {evens_count}."

print(evens_and_odds(100))
# 2 - Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    """This function returns the factorial of the given whole number."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(factorial(5))   
print(factorial(0))   
print(factorial(10))  
# 3 - Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
    """This function checks if the given value is empty."""
    if value is None:
        return True
    elif isinstance(value, str) or isinstance(value, list) or isinstance(value, dict):
        return not bool(value)
    else:
        return False

empty_string = ""
non_empty_string = "Hello"
empty_list = []
non_empty_list = [1, 2, 3]
empty_dict = {}
non_empty_dict = {"key": "value"}

print(is_empty(empty_string))        # Output: True
print(is_empty(non_empty_string))    # Output: False
print(is_empty(empty_list))          # Output: True
print(is_empty(non_empty_list))      # Output: False
print(is_empty(empty_dict))          # Output: True
print(is_empty(non_empty_dict))      # Output: False
print(is_empty(None))                # Output: True
print(is_empty(42))                  # Output: False
# 4 - Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

import statistics

def calculate_mean(data):
    """Calculates the mean (average) of a list."""
    return sum(data) / len(data) if len(data) > 0 else None

def calculate_median(data):
    """Calculates the median of a list."""
    return statistics.median(data) if len(data) > 0 else None

def calculate_mode(data):
    """Calculates the mode of a list."""
    return statistics.mode(data) if len(data) > 0 else None

def calculate_range(data):
    """Calculates the range of a list."""
    return max(data) - min(data) if len(data) > 0 else None

def calculate_variance(data):
    """Calculates the variance of a list."""
    return statistics.variance(data) if len(data) > 0 else None

def calculate_std(data):
    """Calculates the standard deviation of a list."""
    return statistics.stdev(data) if len(data) > 0 else None

data_list = [2, 4, 4, 4, 5, 5, 7, 9]

print("Mean:", calculate_mean(data_list))
print("Median:", calculate_median(data_list))
print("Mode:", calculate_mode(data_list))
print("Range:", calculate_range(data_list))
print("Variance:", calculate_variance(data_list))
print("Standard Deviation:", calculate_std(data_list))

#=============================================================================
#Level 3
#=============================================================================

# 1 - Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    """Checks if the given number is a prime number."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(5))    
print(is_prime(16))   
print(is_prime(23))   
print(is_prime(1))    
print(is_prime(29))   
# 2 - Write a functions which checks if all items are unique in the list.
def are_all_unique(my_list):
    """Checks if all items in the list are unique."""
    return len(my_list) == len(set(my_list))

unique_list = [1, 2, 3, 4, 5]
non_unique_list = [1, 2, 3, 4, 1]

print(are_all_unique(unique_list))      
print(are_all_unique(non_unique_list))  
# 3 - Write a function which checks if all the items of the list are of the same data type.
def are_all_same_type(my_list):
    """Checks if all items in the list are of the same data type."""
    return len(set(map(type, my_list))) == 1 if my_list else False

same_type_list = [1, 2, 3, 4, 5]
mixed_type_list = [1, "apple", 3.14, True]

print(are_all_same_type(same_type_list))      # Output: True
print(are_all_same_type(mixed_type_list))     # Output: False
# 4 - Write a function which check if provided variable is a valid python variable
import re

def is_valid_variable(variable_name):
    """Checks if the provided variable is a valid Python variable name."""
    if not isinstance(variable_name, str):
        return False

    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    
    return bool(pattern.match(variable_name))

valid_variable = "my_variable"
invalid_variable = "123invalid"

print(is_valid_variable(valid_variable))     # Output: True
print(is_valid_variable(invalid_variable))   # Output: False
# 5 - Go to the data folder and access the countries-data.py file.
#       - Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
import re
from collections import Counter
def most_spoken_languages(file_path, top_n=10):
    with open(file_path, 'r', encoding='utf-8') as file:
        python_code = file.read()

    match = re.search(r'\[.*\]', python_code, re.DOTALL)
    if match:
        countries_data_str = match.group(0)
        try:
            countries_data = eval(countries_data_str)
            all_languages = []

            for country_info in countries_data:
                if 'languages' in country_info:
                    all_languages.extend(country_info['languages'])


            language_counter = Counter(all_languages)

           
            most_spoken_languages = language_counter.most_common(top_n)

            return most_spoken_languages

        except SyntaxError:
            print("Error: Unable to evaluate the list of dictionaries.")
    else:
        print("List of dictionaries not found in the Python file.")
        return None

file_path = r'c:\Users\alber\Documents\DocumentsAlbert\CV\Linkedin projects\30daysPython\exercices\someinfo_needed\countries-data.py'
result = most_spoken_languages(file_path, top_n=10)

if result:
    print("Top Ten Most Spoken Languages:")
    for language, count in result:
        print(f"{language}: {count}")
#       - Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
import re
from operator import itemgetter

def most_populated_countries(file_path, top_n=10):
    with open(file_path, 'r', encoding='utf-8') as file:
        python_code = file.read()

    match = re.search(r'\[.*\]', python_code, re.DOTALL)
    if match:
        countries_data_str = match.group(0)
        try:
            countries_data = eval(countries_data_str)

            
            all_populations = [(country_info['name'], country_info['population']) for country_info in countries_data
                               if 'population' in country_info]

            
            sorted_populations = sorted(all_populations, key=itemgetter(1), reverse=True)

            top_n_populated_countries = sorted_populations[:top_n]

            return top_n_populated_countries

        except SyntaxError:
            print("Error: Unable to evaluate the list of dictionaries.")
    else:
        print("List of dictionaries not found in the Python file.")
        return None

file_path = r'c:\Users\alber\Documents\DocumentsAlbert\CV\Linkedin projects\30daysPython\exercices\someinfo_needed\countries-data.py'
result = most_populated_countries(file_path, top_n=10)

if result:
    print("Top 10 Most Populated Countries:")
    for country, population in result:
        print(f"{country}: {population}")
