### Exercices ###

# 1 - Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)
i = 0
while i <= 10:
    print(i)
    i += 1
# 2 - Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)
i = 10
while i >= 0:
    print(i)
    i -= 1
'''
  3 - Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
'''
for i in range(1, 8):
    print("#" * i)
'''
  4 - Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
'''
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()
'''
  5 - Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''
for i in range(11):
    result = i * i
    print(f"{i} x {i} = {result}")
# 6 - Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
programming_languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in programming_languages:
    print(language)
# 7 - Use for loop to iterate from 0 to 100 and print only even numbers
for number in range(0, 101, 2):
    print(number)
# 8 - Use for loop to iterate from 0 to 100 and print only odd numbers
for number in range(1, 101, 2):
    print(number)
    
#=============================================================================
#Level 2
#=============================================================================

# 1 - Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum_of_numbers = 0
for number in range(101):
    sum_of_numbers += number
print("The sum of all numbers from 0 to 100 is:", sum_of_numbers)
#   1.1 - Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_of_evens = 0
sum_of_odds = 0
for number in range(101):
    if number % 2 == 0:
        sum_of_evens += number
    else:
        sum_of_odds += number
print("Sum of even numbers from 0 to 100:", sum_of_evens)
print("Sum of odd numbers from 0 to 100:", sum_of_odds)

#=============================================================================
#Level 3
#=============================================================================

# 1 - Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from someinfo_needed.countries import countries
countries_with_land = [country for country in countries if 'land' in country.lower()]
print("Countries containing 'land':")
for country in countries_with_land:
    print(country)
# 2 - This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in reversed(fruits):
    reversed_fruits.append(fruit)
print("Original list:", fruits)
print("Reversed list:", reversed_fruits)
import re
import json
import sys

file_path = r'c:\Users\alber\Documents\DocumentsAlbert\CV\Linkedin projects\30daysPython\exercices\someinfo_needed\countries-data.py'

with open(file_path, 'r', encoding='utf-8') as file:
    python_code = file.read()

match = re.search(r'\[.*\]', python_code, re.DOTALL)
if match:
    countries_data_str = match.group(0)
    try:
        countries_data = eval(countries_data_str)
        for country_info in countries_data:
            try:
                print(country_info)
            except UnicodeEncodeError:
                print("UnicodeEncodeError: Some characters cannot be displayed.")

    except SyntaxError:
        print("Error: Unable to evaluate the list of dictionaries.")
else:
    print("List of dictionaries not found in the Python file.")

#       3.1 - What are the total number of languages in the data
unique_languages = set()
for country_info in countries_data:
    if 'languages' in country_info:
        unique_languages.update(country_info['languages'])
print("List of unique languages:")
try:
    print(list(unique_languages))
except UnicodeEncodeError:
    print("UnicodeEncodeError: Some characters in the languages cannot be displayed.")
total_languages = len(unique_languages)
print(f'Total number of unique languages: {total_languages}')
#       3.2 - Find the ten most spoken languages from the data
from collections import Counter
all_languages = []
for country_info in countries_data:
    if 'languages' in country_info:
        all_languages.extend(country_info['languages'])
language_counter = Counter(all_languages)
most_spoken_languages = language_counter.most_common(10)
print("Top Ten Most Spoken Languages:")
for language, count in most_spoken_languages:
    print(f"{language}: {count}")
#       3.2 - Find the 10 most populated countries in the world
from operator import itemgetter
all_populations = []
for country_info in countries_data:
    if 'population' in country_info:
        all_populations.append((country_info['name'], country_info['population']))
sorted_populations = sorted(all_populations, key=itemgetter(1), reverse=True)
top_10_populated_countries = sorted_populations[:10]
print("Top 10 Most Populated Countries:")
for country, population in top_10_populated_countries:
    print(f"{country}: {population}")