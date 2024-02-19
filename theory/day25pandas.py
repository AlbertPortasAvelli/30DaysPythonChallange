# Day 25 - Pandas Summary

# 1 - Pandas:
# Pandas is an open-source, high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Pandas adds data structures and tools designed to work with table-like data which is Series and DataFrames. Pandas provides tools for data manipulation:

# 1.1 - Installing Pandas:
# For Mac:
# - `pip install conda`
# - `conda install pandas`
# For Windows:
# - `pip install conda`
# - `pip install pandas`

# 1.2 - Data Structures:
# A series is a column and a DataFrame is a multidimensional table made up of a collection of series.

# 1.3 - Importing Pandas:
import pandas as pd  # importing pandas as pd
import numpy as np   # importing numpy as np

# 1.4 - Creating Pandas Series:
# - With default index:
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
# - With custom index:
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
# - From a dictionary:
dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki'}
s = pd.Series(dct)
# - With a constant value:
s = pd.Series(10, index=[1, 2, 3])
# - Using linspace for numerical sequences:
s = pd.Series(np.linspace(5, 20, 10))  # linspace(starting, end, items)

# 1.5 - Creating DataFrames:
# - From a List of Lists:
data = [['Asabeneh', 'Finland', 'Helsinki'], ['David', 'UK', 'London'], ['John', 'Sweden', 'Stockholm']]
df = pd.DataFrame(data, columns=['Names', 'Country', 'City'])
# - Using a Dictionary:
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country': ['Finland', 'UK', 'Sweden'], 'City': ['Helsinki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
# - From a List of Dictionaries:
data = [{'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'}, {'Name': 'David', 'Country': 'UK', 'City': 'London'}, {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
# - Reading CSV files into DataFrames:
df = pd.read_csv('weight-height.csv')

# 1.6 - Data Exploration:
# Summary statistics using describe():
print(df.describe())
# Information about the DataFrame using info():
print(df.info())
# Modifying DataFrames: Adding, removing, and modifying columns.
df['Height'] = df['Height'] * 0.01
df['BMI'] = df['Weight'] / (df['Height'] ** 2)
# Formating DataFrame columns:
df['BMI'] = round(df['BMI'], 1)
# Checking data types and modifying them:
df['Birth Year'] = df['Birth Year'].astype('int')
df['Current Year'] = df['Current Year'].astype('int')
# Calculating new columns:
df['Age'] = df['Current Year'] - df['Birth Year']
# Boolean indexing for data filtering:
print(df[df['Age'] > 18])
