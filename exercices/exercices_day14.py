### EXERCICES ###
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
1. Explain the difference between map, filter, and reduce.
map: Applies a given function to all items in an iterable and returns an iterator of the results.

filter: Filters elements from an iterable based on a given function that returns True or False.

reduce: Applies a binary function cumulatively to the items of an iterable, reducing it to a single value.

2. Explain the difference between higher-order function, closure, and decorator.
Higher-order function: A function that takes one or more functions as arguments or returns a function as its result.

Closure: A function object that has access to variables in its lexical scope, even after the scope has finished executing.

Decorator: A function that takes another function and extends or modifies the behavior of the latter function without changing its code.
'''
# 3 - Define a call function before map, filter, or reduce, see examples.
def call(func, *args, **kwargs):
    return func(*args, **kwargs)

result = call(len, [1, 2, 3, 4])
print(result)  # Output: 4
# 4 - Use a for loop to print each country in the countries list.
for country in countries:
    print(country)
# 5 - Use a for loop to print each name in the names list.
for name in names:
    print(name)
# 6 - Use a for loop to print each number in the numbers list.
for number in numbers:
    print(number)
#===========================================================================
#Level 2 
#===========================================================================

# 1 - Use map to create a new list by changing each country to uppercase in the countries list.
uppercase_countries = list(map(str.upper, countries))
print(uppercase_countries)
# 2 - Use map to create a new list by changing each number to its square in the numbers list.
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
# 3 - Use map to change each name to uppercase in the names list.
uppercase_names = list(map(str.upper, names))
print(uppercase_names)
# 4 -  Use filter to filter out countries containing 'land'.
filtered_countries_land = list(filter(lambda country: 'land' not in country, countries))
print(filtered_countries_land)
# 5 - Use filter to filter out countries having exactly six characters.
filtered_countries_six_chars = list(filter(lambda country: len(country) != 6, countries))
print(filtered_countries_six_chars)
# 6 -   Use filter to filter out countries containing six letters and more in the country list.
filtered_countries_six_letters = list(filter(lambda country: len(country) >= 6, countries))
print(filtered_countries_six_letters)
# 7 - Use filter to filter out countries starting with an 'E'.
filtered_countries_starting_with_e = list(filter(lambda country: not country.startswith('E'), countries))
print(filtered_countries_starting_with_e)
# 8 - Chain two or more list iterators (e.g., arr.map(callback).filter(callback).reduce(callback)).
result = list(filter(lambda x: x % 2 == 0, map(lambda x: x**2, numbers)))
print(result)
# 9 - Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(my_list):
    return list(filter(lambda item: isinstance(item, str), my_list))
mixed_list = [1, 'apple', 3, 'banana', 'kiwi', '2']
string_list = get_string_lists(mixed_list)
print(string_list)
# 10 - Use reduce to sum all the numbers in the numbers list.
from functools import reduce

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)
# 11 - Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries.
concatenated_countries_sentence = reduce(lambda x, y: f"{x}, {y}", countries)
print(f"{concatenated_countries_sentence} are north European countries.")
# 12 - Declare a function called categorize_countries that returns a list of countries with some common pattern.
def categorize_countries(pattern):
    return list(filter(lambda country: pattern.lower() in country.lower(), countries))

patterned_countries = categorize_countries('land')
print(patterned_countries)
# 13 - Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def starting_letter_count_dict(country_list):
    starting_letters = [country[0].upper() for country in country_list]
    letter_count_dict = {letter: starting_letters.count(letter) for letter in set(starting_letters)}
    return letter_count_dict

starting_letter_count = starting_letter_count_dict(countries)
print(starting_letter_count)
# 14 - Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
import ast

def get_first_ten_countries():
    with open(r'C:\Users\alber\Documents\DocumentsAlbert\CV\Linkedin projects\30daysPython\exercices\someinfo_needed\countries.py', 'r') as file:
        try:
            countries_data = ast.literal_eval(file.read())
            return countries_data[:10]
        except (SyntaxError, ValueError):
            print("Error: Unable to evaluate the literal expression in the file.")
            return None

first_ten_countries = get_first_ten_countries()

if first_ten_countries:
    print("First Ten Countries:")
    for country in first_ten_countries:
        print(country)
# 15 - Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries():
    with open(r'C:\Users\alber\Documents\DocumentsAlbert\CV\Linkedin projects\30daysPython\exercices\someinfo_needed\countries.py', 'r') as file:
        try:
            countries_data = ast.literal_eval(file.read())
            return countries_data[-10:]
        except (SyntaxError, ValueError):
            print("Error: Unable to evaluate the literal expression in the file.")
            return None

last_ten_countries = get_last_ten_countries()

if last_ten_countries:
    print("Last Ten Countries:")
    for country in last_ten_countries:
        print(country)
#============================================================================
#Level 3
#============================================================================

'''# 1 - Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
Sort countries by name, by capital, by population
Sort out the ten most spoken languages by location.
Sort out the ten most populated countries.'''
import re
from collections import Counter

def sort_countries_by_name(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        python_code = file.read()

    match = re.search(r'\[.*\]', python_code, re.DOTALL)
    if match:
        countries_data_str = match.group(0)
        try:
            countries_data = eval(countries_data_str)
            sorted_countries_by_name = sorted(countries_data, key=lambda x: x['name'])
            return sorted_countries_by_name

        except SyntaxError:
            print("Error: Unable to evaluate the list of dictionaries.")
    else:
        print("List of dictionaries not found in the Python file.")
        return None

def sort_countries_by_capital(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        python_code = file.read()

    match = re.search(r'\[.*\]', python_code, re.DOTALL)
    if match:
        countries_data_str = match.group(0)
        try:
            countries_data = eval(countries_data_str)
            sorted_countries_by_capital = sorted(countries_data, key=lambda x: x.get('capital', ''))
            return sorted_countries_by_capital

        except SyntaxError:
            print("Error: Unable to evaluate the list of dictionaries.")
    else:
        print("List of dictionaries not found in the Python file.")
        return None

def sort_countries_by_population(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        python_code = file.read()

    match = re.search(r'\[.*\]', python_code, re.DOTALL)
    if match:
        countries_data_str = match.group(0)
        try:
            countries_data = eval(countries_data_str)
            sorted_countries_by_population = sorted(countries_data, key=lambda x: x.get('population', 0), reverse=True)
            return sorted_countries_by_population

        except SyntaxError:
            print("Error: Unable to evaluate the list of dictionaries.")
    else:
        print("List of dictionaries not found in the Python file.")
        return None

file_path = r'c:\Users\alber\Documents\DocumentsAlbert\CV\Linkedin projects\30daysPython\exercices\someinfo_needed\countries-data.py'

result_sorted_by_name = sort_countries_by_name(file_path)
result_sorted_by_capital = sort_countries_by_capital(file_path)
result_sorted_by_population = sort_countries_by_population(file_path)


if result_sorted_by_name:
    print("\nCountries Sorted by Name:")
    for country_info in result_sorted_by_name:
        try:
            print(country_info['name'])
        except UnicodeEncodeError:
            print("Unable to print country name due to encoding error.")

if result_sorted_by_capital:
    print("\nCountries Sorted by Capital:")
    for country_info in result_sorted_by_capital:
        try:
            print(country_info['name'] + " " + country_info['capital'])
        except UnicodeEncodeError:
            print("Unable to print country name due to encoding error.")
if result_sorted_by_population:
    print("\nCountries Sorted by Name:")
    for country_info in result_sorted_by_population:
        try:
            print(f"{country_info['name']}: {country_info.get('population', 0)}")

        except UnicodeEncodeError:
            print("Unable to print country name due to encoding error.")
