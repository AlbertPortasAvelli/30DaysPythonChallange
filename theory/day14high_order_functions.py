### High Order Functions ###
# functions are functions that operate on other functions by taking them as arguments or returning them as results.

# 1 - Function as a Parameter
def square(x):
    return x * x

def cube(x):
    return x * x * x

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(square, numbers)
# squared_numbers is now [1, 4, 9, 16, 25]

cubed_numbers = map(cube, numbers)
# cubed_numbers is now [1, 8, 27, 64, 125]
# 2 - Function as a Return Value
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)

triple = multiplier(3)

result_double = double(4)  # result_double is 8
result_triple = triple(4)  # result_triple is 12
# 3 - Python Closures
#a function object that has access to variables in its lexical scope, even when the function is called outside that scope.
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Create a closure by calling outer_function
closure_instance = outer_function(10)

# Use the closure to perform computations
result = closure_instance(5)  # result is 15
# 4 - Python Decorators
# powerful and flexible way to modify or extend the behavior of functions or methods.
def log_arguments_and_result(func):
    def wrapper(*args, **kwargs):
        # Log the arguments
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Log the result
        print(f"{func.__name__} returned: {result}")
        
        return result

    return wrapper

# Applying the decorator using the @ syntax
@log_arguments_and_result
def add(a, b):
    return a + b

@log_arguments_and_result
def multiply(x, y):
    return x * y

# Using the decorated functions
result_add = add(3, 5)
result_multiply = multiply(4, 6)
'''
You can apply multiple decorators to a function in Python by stacking them on the same line or writing them one below the other.
Decorators are applied from bottom to top, with the bottom decorator being the outermost layer.
The order of decorators matters because each decorator modifies the behavior of the function.
When decorators are stacked on the same line, they are executed from right to left. The rightmost decorator is applied first, and the result is passed to the decorator on its left.
Stacking decorators on the same line is a concise and common practice in Python.
'''
# 5 - Built-in Higher Order Functions
# are functions that take other functions as arguments or return functions as results. 
# Using map to double each element in a list
numbers = [1, 2, 3, 4]
doubled_numbers = map(lambda x: x * 2, numbers)
result = list(doubled_numbers)
print(result)  # Output: [2, 4, 6, 8]
# Using filter to keep only even numbers in a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
result = list(even_numbers)
print(result)  # Output: [2, 4, 6]
from functools import reduce
# Using reduce to find the product of elements in a list
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24 (1 * 2 * 3 * 4)