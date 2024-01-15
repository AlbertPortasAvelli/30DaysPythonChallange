import math

### Strings ###
#string is a sequence of characters. It is a data type that represents textual data and is enclosed in either single quotes (') or double quotes ("). 

#   1 - String Concetanation
#       the process of combining two or more strings into a single string. 
salutation = 'Hello! '
presentation = 'My name is Harold '
phrase = salutation + presentation
print(phrase)
#   2 - Escape Sequences in Strings
#        special combinations of characters that represent characters that are difficult or impossible to include directly in a string. 
#       2.1 - New Line (\n)
print('Hello\nWorld')
#       2.2 - Tab (\t)
print('Hello\tWorld')
#       2.3 - Single Quote (\')
print('There\'s a lot of people today')
#       2.4 - Double Quote (\")
print('The captain said : \"Are you all cowards?\"')
#   3 - String Formatting
#       refers to the process of creating a formatted string by embedding expressions
#       inside a string literal. It allows you to interpolate values into a string
#       and control the way they are presented. 

#       3.1 - Old Formatting - %s(string), %d(integers), %f(float), %.num of digitsf(float fixing point numbers)
name = 'Albert'
age = 30
height = 1.84
pi = math.pi
print('Hello! I\'m %s and i\'m %d years old, also i\'m %f meters tall and it is %.2f pm'%(name, age, height, pi))
#       3.2 - New Formatting (str.format)
print('Hello! I\'m {} and i\'m {} years old, also i\'m {} meters tall and it is {} pm'.format(name, age, height, pi))
#       3.3 - String Interpolation / f-Strings
print(f'Hello! I\'m {name} and i\'m {age} years old, also i\'m {height} meters tall and it is {pi} pm')
#   4 - Characteristics
#       4.1 - Unpacking Characters
language = 'Python'
a, b, c, d, e, f = language
print(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}')
#       4.2 - Accessing Characters in Strings by Index
print(f'{language[0]}\n{language[-1]}\n{language[-4]}\n{language[3]}')
#       4.3 - Slicing Python Strings
print(f'{language[0:3]}\n{language[3:6]}\n{language[-3:]}')
#       4.4 - Reversing a String
print(f'{language[::-1]}')
#       4.5 - Skipping Characters While Slicing
print(f'{language[0:3:6]}')
#   5 - String Methods
#       5.1 - capitalize()
print(language.capitalize)
#       5.2 - count()
challange = 'thirty days of python'
print(challange.count('y'))
#       5.3 - endswith()
print(challange.endswith('on'))
#       5.4 - expandstabs()
print(challange.expandtabs(10))
#       5.5 - find()
# Returns the index of the first occurrence of a substring, if not found returns -1
print(challange.find('y'))
#       5.6 - rfind()
#Returns the index of the last occurrence of a substring, if not found returns -1
print(challange.rfind('y'))
#       5.7 - format()
#already explained on the lines 27 to 37
#       5.8 - index()
#Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). 
#If the substring is not found it raises a valueError.
sub_string = 'da'
print(challange.index(sub_string))
#       5.9 - rindex()
#Returns the highest index of a substring, 
#additional arguments indicate starting and ending index (default 0 and string length - 1)
print(challange.rindex(sub_string))
#       5.10 - isalnum()
challenge_two = '30DaysPython'
print(challange.isalnum())
print(challenge_two.isalnum())
#       5.11 - isalpha()
num = '123'
print(challange.isalpha())
print(challenge_two.isalpha())
print(num.isalpha)
#       5.12 - isdecimal()
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed
#       5.13 - isdigit()
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
#       5.14 - isnumeric()
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
#       5.15 - isidentifier()
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
#       5.16 - islower()
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
#       5.17 - isupper()
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
#       5.18 - join()
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
#       5.19 - strip()
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'
#       5.20 - replace()
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
#       5.21 - split()
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
#       5.22 - title()
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
#       5.23 - swapcase()
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
#       5.24 - startswith()
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False