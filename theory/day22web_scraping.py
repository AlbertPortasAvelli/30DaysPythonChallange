### Web Screping ###

#is the process of extracting data from websites.


'''
Basic Steps:

    - Install required packages using pip.
    - Import necessary modules (requests and BeautifulSoup).
    - Define the URL of the website to be scraped.
    - Use requests.get() method to fetch the HTML content of the webpage.
    - Parse the HTML content using BeautifulSoup to extract desired data.
'''
# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of the website to be scraped
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Use requests.get() to fetch the webpage
response = requests.get(url)

# Check the status code to ensure the request was successful
status = response.status_code
print(status)  # 200 means the fetching was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Print the title of the webpage
print(soup.title.get_text())  # Output: UCI Machine Learning Repository: Data Sets

# Print the body of the webpage
print(soup.body)

# Extract data from tables
tables = soup.find_all('table', {'cellpadding': '3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class, or HTML tag for more information check the BeautifulSoup doc
table = tables[0]  # The result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)
