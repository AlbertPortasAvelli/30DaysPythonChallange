### Python Package Manager ###

# 1 - What is PIP ?

#PIP stands for Preferred installer program. We use pip to install different Python packages. 

# 2 - Install PIP

#Go to your terminal or command prompt and copy and paste this: 
#pip install pip

# Check if pip is installed by writing
#pip --version

# 3 - Installing packages using pip

#pip install numpy

#pip install pandas

# 4 - Uninstalling Packages

#pip uninstall packagename

# 5 - List of Packages

#pip list

# 6 - Show Package

# pip show packagename

#If we want even more details, just add --verbose

# 7 - PIP Freeze

#pip freeze

#The pip freeze gave us the packages used, installed and their version.
#We use it with requirements.txt file for deployment.

# 8 - Reading from URL

#pip install requests

import requests # importing the request module

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page

# 9 - Creating a Package

#Create a new folder named mypacakge inside 30DaysOfPython folder Create an empty init.py file in the mypackage folder. 
#Create modules arithmetic.py and greet.py


# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


def subtract(a, b):
    return (a - b)


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


def remainder(a, b):
    return a % b


def power(a, b):
    return a ** b

# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'

#folder structure : 
'''
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
'''

'''
asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from mypackage import arithmetics
>>> arithmetics.add_numbers(1, 2, 3, 5)
11
>>> arithmetics.subtract(5, 3)
2
>>> arithmetics.multiple(5, 3)
15
>>> arithmetics.division(5, 3)
1.6666666666666667
>>> arithmetics.remainder(5, 3)
2
>>> arithmetics.power(5, 3)
125
>>> from mypackage import greet
>>> greet.greet_person('Asabeneh', 'Yetayeh')
'Asabeneh Yetayeh, welcome to 30DaysOfPython Challenge!'
>>>
'''

# 10 - Important packages

'''
Database:
    SQLAlchemy or SQLObject - Object oriented access to several different database systems
        pip install SQLAlchemy

Web Development:
    Django - High-level web framework
        pip install django
    Flask - Micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
        pip install flask

HTML Parser:
    Beautiful Soup - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.
        pip install beautifulsoup4
    PyQuery - Implements jQuery in Python; faster than BeautifulSoup, apparently.

XML Processing:
    ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the Standard Library

GUI:
    PyQt - Bindings for the cross-platform Qt framework
    TkInter - The traditional Python user interface toolkit

Data Analysis, Data Science and Machine learning:
    Numpy: Numeric Python is known as one of the most popular machine learning library in Python
    Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis
    SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics
    Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data
    TensorFlow: is a machine learning library built by Google
    Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more

Network:
    requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)
        pip install requests
'''