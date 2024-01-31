### Python Error Type ###
#errors are classified into three main types: syntax errors, runtime errors, and logical errors. 

# 1 - SyntaxError
#  Syntax errors occur when the code violates the Python language rules. 
#  print("Hello, world!"

# 2 - NameError
#   occurs when the interpreter encounters a name that is not defined or not recognized within the current scope. 
'''
x = 42
print(x)
'''

# 3 - IndexError
#   ccurs when you try to access an index in a sequence that is outside the valid range of indices for that sequence. 
'''
my_list = [1, 2, 3]
print(my_list[5])
'''

# 4 - ModuleNotFoundError
#   occurs when the interpreter cannot find the module you are trying to import in your code.

#import non_existent_module

# 5 - AttributeError
#   occurs when you try to access or use an attribute of an object, and that attribute does not exist for the given object.

'''
class MyClass:
    pass

obj = MyClass()
print(obj.some_attribute)
'''

# 6 - KeyError
#    when you try to access a dictionary key that does not exist.

#my_dict = {'a': 1, 'b': 2, 'c': 3}
#value = my_dict['d']

# 7 - TypeError
#    when an operation or function is applied to an object of an inappropriate type.

#result = '5' + 3

# 8 - ImportError
#   when the interpreter encounters an issue while trying to import a module.

#import NumPy 

# 9 - ValueError
#   is raised when a function receives an argument of the correct type but with an inappropriate value.

#int("abc")

# 10 - ZeroDivisionError
#   attempt to divide a number by zero. 
#result = 5 / 0