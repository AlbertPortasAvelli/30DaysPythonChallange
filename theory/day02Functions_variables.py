### Functions and Variables ###

'''
    1 - Functions
        functions are blocks of reusable code that perform a specific task.
        Python comes with several built-in functions that are part of the 
        Python Standard Library. These functions are readily available for
        you to use without the need for additional installations or imports.
'''
# 1 - Examples

#   1.1 - len()
#       Returns the length (number of items) of an object.

length = len([1, 2, 3, 4, 5])
print(length)

#   1.2 - max() and min()
#       Return the maximum and minimum values from an iterable or a series of arguments.

maximum = max(4, 7, 1, 9, 3)
minimum = min([2, 5, 8, 1, 6])
print('max : {}\nmin : {}'.format(maximum, minimum))

#   1.3 - sorted()
#       Returns a new sorted list from the elements of any iterable.

sorted_list = sorted([3, 1, 4, 1, 5, 9, 2])
print(sorted_list)

#   1.4 - abs()
#       Returns the absolute value of a number.

absolute_value = abs(-10)

#   1.5 - map()
#       Applies a specified function to all items in an input iterable and returns an iterator of the results.

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)

print(list(squared))

#   1.6 - filter()
#       Filters elements of an iterable based on a function's criteria.

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))

#   1.7 - zip()
#       Combines multiple iterables into tuples, where each tuple contains elements from the input iterables at the same position.

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
combined = zip(names, ages)

print(list(combined))

#   1.8 - enumerate()
#       Returns an iterator that yields pairs of index and element, useful for iterating over elements along with their index.

words = ["apple", "banana", "cherry"]
for index, value in enumerate(words):
    print(f"Index: {index}, Value: {value}")

#   1.9 - any() and all()
#       Check if any or all elements of an iterable are True.
    
bool_list = [True, False, True, True]
any_true = any(bool_list)
all_true = all(bool_list)
print('There\'s any true? : {}\nAre they all true?: {} '.format(any_true, all_true))

#   1.10 - sum() with a starting value 
#       Calculate the sum of elements with an initial value.

numbers = [1, 2, 3, 4, 5]
sum_with_initial = sum(numbers, 10)
print(sum_with_initial)

#   1.11 - sorted() with a custom key function
#       Sort elements based on a custom key function.

words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))

print(list(sorted_words))


# 2 - Variables
#   In Python, variables are used to store and manage data in a program. 
#   A variable is essentially a named storage location that holds a value.

#   2.1 - Variable Rules
#       - A variable name must start with a letter or the underscore character
#       - A variable name cannot start with a number
#       - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#       - Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

#   2.2 - Declaring Multiple Variable in a Line
first_name, last_name, country, age = 'Albert', 'Portas', 'Spain', 30
print('Name : {}\nLast Name: {}\nAge : {}\nCountry : {}'.format(first_name, last_name, age, country))


#   2.3 - Checking Data types and Casting
#       2.3.1 - Checking Data Type
#           o check the data type of certain data we use the method type()

x = 5
y = "10"

print("Type of x:", type(x))
print("Type of y:", type(y))

#       2.3.2 - Casting
#           Converting one data type to another data type. We use int(), float(), str(), list(), set()

result = x + int(y)
y = int(y)
print(type(y))