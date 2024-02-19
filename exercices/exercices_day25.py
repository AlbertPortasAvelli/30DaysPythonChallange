import pandas as pd

# Read the hacker_news.csv file from data directory
df = pd.read_csv("C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\exercices\\data\\hacker_news.csv")

# Get the first five rows
first_five_rows = df.head()

# Get the last five rows
last_five_rows = df.tail()

# Get the title column as pandas series
title_series = df['title']

# Count the number of rows and columns
num_rows, num_columns = df.shape

# Filter the titles which contain 'python'
python_titles = df[df['title'].str.contains('python', case=False)]

# Filter the titles which contain 'JavaScript'
javascript_titles = df[df['title'].str.contains('JavaScript', case=False)]

# Explore the data and make sense of it
# You can explore various aspects of the data, such as summary statistics, unique values, etc.
summary_statistics = df.describe()
unique_authors = df['author'].unique()

# Print the results
print("First five rows:\n", first_five_rows)
print("\nLast five rows:\n", last_five_rows)
print("\nTitle column as pandas series:\n", title_series)
print("\nNumber of rows:", num_rows)
print("Number of columns:", num_columns)
print("\nTitles containing 'python':\n", python_titles)
print("\nTitles containing 'JavaScript':\n", javascript_titles)
print("\nSummary statistics:\n", summary_statistics)
print("\nUnique authors:\n", unique_authors)
