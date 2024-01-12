### Day 1 of 30 day Python Challange ###

# 1- Comments
#   1.1 - Single comments
#       Single line comments has to start with a hash (#) like this line.
#   1.2 - Multiple comments
'''Multiple comments use the triple quote for write a comment that 
        extends more than a line. You can use simple quote (') 
        or the double quote(")'''
# 2 - Data types
#   There are a lot types of data in python this are the most common ones.
#   2.1 - Numbers
#       You can use three types of numbers.
#       2.1.1 - Integer
#           You can type the integers numbers as the name says.

integer_number :int= 1
print(type(integer_number))

#       2.1.2 - Float
#           This type of data will allow you to use numbers with decimals

float_number :float = 2.66
print(type(float_number))

#       2.1.3 - Complex 
#           Can be used for make some operations like (1 + j)

complex_number :complex = (1 + 1j)
print(type(complex_number))

#   2.2 - Strings
#       Collection of one or more characters under single or double quote

string_example = 'Albert'
longer_example = "I am enjoying the 30DaysOfPython Challenge"
print(type(string_example))

#   2.3 - Booleans
#       Can be only two things True or False (remember to use the uppercase on T for True and in F for False)

true_boolean = True
false_boolean = False
print(type(true_boolean))

#   2.4 - List
#       Ordered collection that store different data type items.

numbers_list = [0, 1, 2, 3, 4, 5]
fruits_list = ['Banana', 'Orange', 'Strawberry', 'Avocado']
my_info_list = ['Albert', 'Portas', 30, 1.84]
print(type(numbers_list))

#   2.5 - Dicctionary
#       Undordered collection of data in a key value pair format(it means each value has a unique identifier called key)

my_info_dictionary = {
    'first_name': 'Ablert',
    'last_name' : 'Portas',
    'country' : 'Spain',
    'age' : 30,
    'skills': ['JS', 'React', 'SQLite']
}
print(type(my_info_dictionary))

#   2.6 - Tuple
#       Similar to list data type because tuples are an ordered collection but they can not be modified once created (immutable)

planets_tuples = ('Earth', 'Jupiter', 'Neptune', 'Mars', 'Saturn', 'Uranus', 'Mercury')
print(type(planets_tuples))

#   2.7 - Set
#       Similar to tuple and lists but is not an ordered collection of items and stores ony unique items

my_nubers_set = {2, 4, 5, 6}
print(type(my_nubers_set))