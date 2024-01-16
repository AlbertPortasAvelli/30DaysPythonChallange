### Exercices ###
#   1 - Declare an empty list
unknown_list = list()
#   2 - Declare a list with more than 5 items
scores = [23, 12, 30, 26, 28]
#   3 - Find the length of your list
print(len(scores))
#   4 - Get the first item, the middle item and the last item of the list
first_item = scores[0]
middle_item = scores[len(scores) // 2]
last_item = scores[-1]
#   5 - Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Albert', 30, 1.84, 'single', 'girona']
#   6 - Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'IBM', 'Amazon']
#   7 - Print the list using print()
print(it_companies)
#   8 - Print the number of companies in the list
print(f'Number of companies : {len(it_companies)}')
#   9 - Print the first, middle and last company
print(f'First company : {it_companies[0]}\nSecond company : {it_companies[len(it_companies) // 2]}\nLast company : {it_companies[len(it_companies) - 1]}')
#   10 - Print the list after modifying one of the companies
it_companies[2] = 'Twitter'
#   11 - Add an IT company to it_companies
it_companies.append('Microsoft')
#   12 - Insert an IT company in the middle of the companies list
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Salesforce')
#   13 - Change one of the it_companies names to uppercase (IBM excluded!)
microsoft_index = it_companies.index('Microsoft')
it_companies[microsoft_index] = it_companies[microsoft_index].upper()
print(it_companies)
#    14 - Join the it_companies with a string '#;  '
joined_companies = '#; '.join(it_companies)
print(joined_companies)
#    15 - Check if a certain company exists in the it_companies list.
company_to_check = 'Google'
if company_to_check in it_companies:
    print(f'{company_to_check} exists in the list.')
else:
    print(f'{company_to_check} does not exist in the list.')
#   16 - Sort the list using sort() method
print(it_companies.sort())
#   17 - Reverse the list in descending order using reverse() method
print(it_companies.reverse())
#   18 - Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print(first_three_companies)
#   19 - Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print(last_three_companies)
#   20 - Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
     middle_companies = it_companies[middle_index - 1:middle_index + 1]
else:
     middle_companies = [it_companies[middle_index]]
print(middle_companies)
#   21 - Remove the first IT company from the list
it_companies.pop(0)
#   22 - Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[middle_index - 1:middle_index + 1]
else:
    del it_companies[middle_index]
print("Updated list:", it_companies)
#   23 - Remove the last IT company from the list
print(it_companies.pop())
#   24 - Remove all IT companies from the list
it_companies.clear()
#   25 - Destroy the IT companies list
del it_companies
#   26 - Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
#   27 - After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack_copy = full_stack.copy()
index_of_redux = full_stack_copy.index('Redux')
full_stack_copy.insert(index_of_redux + 1, 'Python')
full_stack_copy.insert(index_of_redux + 2, 'SQL')
print("Modified list:", full_stack_copy)
#============================================================================
#Level 2
#============================================================================

#   1 - The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#       - Sort the list and find the min and max age
ages_sorted = ages.sort()
min_age = min(ages)
max_age = max(ages)
#       - Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
#       - Find the median age (one middle item or two middle items divided by two)
length = len(ages)
middle_index = length // 2
if length % 2 == 0:
    median_age = (ages[middle_index - 1] + ages[middle_index]) / 2
else:
    median_age = ages[middle_index]
#       - Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
#       - Find the range of the ages (max minus min)
age_range = max_age - min_age
#       - Compare the value of (min - average) and (max - average), use abs() method
min_difference = abs(min_age - average_age)
max_difference = abs(max_age - average_age)
print("Absolute difference between min and average age:", min_difference)
print("Absolute difference between max and average age:", max_difference)
#   2 - Find the middle country(ies) in the countries list
from someinfo_needed.countries import countries
length = len(countries)
middle_index = length // 2
if length % 2 == 0:
    middle_countries = countries[middle_index - 1:middle_index + 1]
else:
    middle_countries = [countries[middle_index]]
print("Middle country(ies):", middle_countries)
#   3 - Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[:middle_index + (length % 2)]
second_half = countries[middle_index + (length % 2):]
print("First half of countries:", first_half)
print("Second half of countries:", second_half)
#   4 - ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
first_country, second_country, third_country, *scandic_countries = countries
print("First country:", first_country)
print("Second country:", second_country)
print("Third country:", third_country)
print("Scandic countries:", scandic_countries)