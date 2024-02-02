### Exeption Handling ###
# is a mechanism that allows you to gracefully manage and respond to errors or exceptional situations that may occur during the execution of a program.

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I always run.')

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

# 1 - Packing and Unpacking Arguments in Python
#   1.1 - Unpacking
#        extracting values from a data structure and assigning them to individual variables.
#       1.1.1 - Unpacking Lists 
numbers = [1, 2, 3, 4, 5]
first, *rest = numbers
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)    #  Output: 1 [2, 3, 4, 5, 6] 7

#       1.1.2 - Unpacking Dictionaries
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(**my_dict)  # Output: a=1 b=2 c=3
#   1.2 - Packing
#       the process of combining multiple values into a single variable
#       1.2.1 - Packing Lists
def pack_list_example(*args):
    print("Packed values:", args)
    total = sum(args)
    print("Total sum:", total)

numbers = [1, 2, 3, 4, 5]
pack_list_example(*numbers)
# Output:
# Packed values: (1, 2, 3, 4, 5)
# Total sum: 15

#       1.2.2 - Packing Dictionaries

def pack_dict_example(**kwargs):
    print("Packed dictionary:", kwargs)
    for key, value in kwargs.items():
        print(f"Key: {key}, Value: {value}")

my_dict = {'a': 1, 'b': 2, 'c': 3}
pack_dict_example(**my_dict)
# Output:
# Packed dictionary: {'a': 1, 'b': 2, 'c': 3}
# Key: a, Value: 1
# Key: b, Value: 2
# Key: c, Value: 3

# 2 - Spreading in Python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# 3 - Enumerate
#a built-in function in Python that is used to iterate over a sequence (such as a list, tuple, or string) while keeping track of the index of the current item.
countries = ['USA', 'Canada', 'Australia', 'India']

for index, country in enumerate(countries):
    print(f"Index {index}: {country}")

# 4 - Zip
#another built-in function in Python that is used to combine elements from two or more iterables into tuples. 
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

# Using zip to combine names and ages into tuples
combined_data = zip(names, ages)

# Converting the zip result to a list for easier viewing
result_list = list(combined_data)

print(result_list)