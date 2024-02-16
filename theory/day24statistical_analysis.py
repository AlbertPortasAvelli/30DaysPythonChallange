### Statistical Analysis ###

# 1 - Python for Statistical Analysis

# 1.1 - Statistics
# Statistics is the discipline that studies the collection, organization, displaying, analysing, interpretation and presentation of data. Statistics is a branch of Mathematics that is recommended to be a prerequisite for data science and machine learning. Statistics is a very broad field but we will focus in this section only on the most relevant part. After completing this challenge, you may go onto the web development, data analysis, machine learning and data science path. Whatever path you may follow, at some point in your career you will get data which you may work on. Having some statistical knowledge will help you to make decisions based on data, data tells as they say.

# 1.2 - Data
# What is data? Data is any set of characters that is gathered and translated for some purpose, usually analysis. It can be any character, including text and numbers, pictures, sound, or video. If data is not put in a context, it doesn't make any sense to a human or computer. To make sense from data we need to work on the data using different tools.

# 1.3 - The work flow of data analysis, data science or machine learning starts from data. Data can be provided from some data source or it can be created. There are structured and unstructured data.

# 1.4 - Data can be found in small or big format. Most of the data types we will get have been covered in the file handling section.

# 2 - Statistics Module

# 2.1 - The Python statistics module provides functions for calculating mathematical statistics of numerical data. The module is not intended to be a competitor to third-party libraries such as NumPy, SciPy, or proprietary full-featured statistics packages aimed at professional statisticians such as Minitab, SAS and Matlab. It is aimed at the level of graphing and scientific calculators.

# 3 - NumPy

# 3.1 - Importing NumPy
# How to import numpy
import numpy as np

# 3.2 - How to check the version of the numpy package
print('numpy:', np.__version__)

# 3.3 - Checking the available methods
print(dir(np))

# 3.4 - Creating numpy array using

# 3.4.1 - Creating int numpy arrays
# Creating python List
python_list = [1,2,3,4,5]

# Checking data types
print('Type:', type(python_list)) # <class 'list'>
print(python_list) # [1, 2, 3, 4, 5]

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Creating Numpy(Numerical Python) array from python list

numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))   # <class 'numpy.ndarray'>
print(numpy_array_from_list) # array([1, 2, 3, 4, 5])

# 3.4.2 - Creating float numpy arrays
# Creating a float numpy array from list with a float data type parameter

# Python list
python_list = [1,2,3,4,5]

numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])

# 3.4.3 - Creating boolean numpy arrays
# Creating a boolean a numpy array from list

numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False,  True,  True, False, False])

# 3.4.4 - Creating multidimensional array using numpy
# A numpy array may have one or multiple rows and columns

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)
# <class 'numpy.ndarray'>
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

# 3.4.5 - Converting numpy array to list
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# 3.5 - Accessing Numpy arrays

# 3.5.1 - Accessing the first element in a numpy array
print(numpy_array_from_list[0]) # 1

# 3.5.2 - Accessing the last element in a numpy array
print(numpy_array_from_list[-1]) # 5

# 3.5.3 - Accessing elements from a two-dimensional array
# To access an element from a two-dimensional array we need to pass two indexes.
# The first one is for the row and the second one is for the column.
print(numpy_two_dimensional_list[0,0]) # 0
print(numpy_two_dimensional_list[0,1]) # 1
print(numpy_two_dimensional_list[0,2]) # 2

# If we want to access all the elements from the first row we can use:
print(numpy_two_dimensional_list[0,:]) # [0 1 2]

# If we want to access all the elements from the first column we can use:
print(numpy_two_dimensional_list[:,0]) # [0 3 6]

# If we want to access all the elements from the second column we can use:
print(numpy_two_dimensional_list[:,1]) # [1 4 7]

# If we want to access all the elements from the third column we can use:
print(numpy_two_dimensional_list[:,2]) # [2 5 8]

# 3.6 - Basic mathematical operations on numpy arrays
# Addition
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a + b) # [5 7 9]

# Subtraction
print(a - b) # [-3 -3 -3]

# Multiplication
print(a * b) # [ 4 10 18]

# Division
print(a / b) # [0.25 0.4  0.5 ]

# Square root
print(np.sqrt(a)) # [1.         1.41421356 1.73205081]

# Mean
print(np.mean(a)) # 2.0

# Median
print(np.median(a)) # 2.0

# Variance
print(np.var(a)) # 0.6666666666666666

# Standard deviation
print(np.std(a)) # 0.816496580927726

# 3.7 - Sorting Numpy arrays
# In order to sort a numpy array we can use the sort() method.

# 3.7.1 - One dimensional arrays
x = np.array([3, 1, 2])
x.sort()
print(x) # [1 2 3]

# 3.7.2 - Two dimensional arrays
y = np.array([[3, 1, 2], [6, 4, 5]])
y.sort(axis=0)
print(y)
# [[3 1 2]
#  [6 4 5]]

y.sort(axis=1)
print(y)
# [[1 2 3]
#  [4 5 6]]

# 3.8 - Slicing
# We can access a range of elements using slicing.

a = np.array([1,2,3,4,5,6,7])
print(a[1:5]) # [2 3 4 5]

# 3.8.1 - Slicing two-dimensional arrays
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a[0:2, 1:3])
# [[2 3]
#  [6 7]]

# 3.9 - Generating random numbers using numpy
# To generate random numbers using numpy we can use the random module.

# 3.9.1 - Generating random float between 0 and 1
print(np.random.rand(5)) # [0.33127366 0.63083542 0.39291952 0.7808084  0.47144332]

# 3.9.2 - Generating random integer between 1 and 100
print(np.random.randint(1, 100)) # 17

# 3.9.3 - Generating random float from normal distribution
print(np.random.randn(5)) # [ 0.07968888  0.12042146 -0.15753652 -1.12915789  1.39677436]

# 3.9.4 - Generating random numbers from 0 to 1 with shape(2,3)
print(np.random.random(size=(2,3)))
# [[0.36857132 0.89170497 0.05507357]
#  [0.85616191 0.19654558 0.17263953]]
