### Functions ###
# reusable block of code that performs a specific task. 
# 1 - Declaring and Calling a Function
# Function declaration
def greet(name):
    """This function takes a name as a parameter and prints a greeting."""
    print(f"Hello, {name}!")

# Function call
greet("Alice")
greet("Bob")
# 2 - Function without Parameters
def greet():
    """This function prints a generic greeting."""
    print("Hello, how are you today?")
# 3 - Function Returning a Value
def add_numbers(a, b):
    """This function takes two numbers as parameters and returns their sum."""
    result = a + b
    return result
sum_result = add_numbers(3, 5)
# 4 - Function with Parameters
def greet_person(name, greeting="Hello"):
    """This function takes a person's name and an optional greeting, and prints a personalized message."""
    print(f"{greeting}, {name}!")
greet_person("Alice")
greet_person("Bob", "Hi")
# 5 - Passing Arguments with Key and Value
def greet_person(name, greeting="Hello", punctuation="!"):
    """This function takes a person's name and optional greetings with custom punctuation."""
    message = f"{greeting}, {name}{punctuation}"
    print(message)
greet_person(name="Alice")
greet_person(name="Bob", greeting="Hi", punctuation="!!!")
# 6 - Function with Default Parameters
def greet_person(name, greeting="Hello", punctuation="!"):
    """This function takes a person's name and optional greetings with custom punctuation."""
    message = f"{greeting}, {name}{punctuation}"
    print(message)
greet_person("Alice")
# 7 - Arbitrary Number of Arguments
def add_numbers(*args):
    """This function takes any number of arguments and returns their sum."""
    result = sum(args)
    return result
sum_result_1 = add_numbers(1, 2, 3)
sum_result_2 = add_numbers(4, 5, 6, 7, 8)
# 8 - Function as a Parameter of Another Function
def square(x):
    """This function returns the square of a number."""
    return x ** 2

def cube(x):
    """This function returns the cube of a number."""
    return x ** 3

def apply_operation(number, operation):
    """This function applies the given operation to the number."""
    result = operation(number)
    return result
result_square = apply_operation(4, square)
result_cube = apply_operation(3, cube)