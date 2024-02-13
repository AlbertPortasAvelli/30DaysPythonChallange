### Exercices ###

# 1 - Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
import requests
from bs4 import BeautifulSoup
import json

# Define the URL of the website to be scraped
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# Use requests.get() to fetch the webpage
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the section containing the facts and stats
facts_section = soup.find('section', {'id': 'facts-stats'})

# Check if the facts_section is None
if facts_section is not None:
    # Initialize a dictionary to store the extracted data
    data = {}

    # Loop through all the facts and stats and extract the text
    for item in facts_section.find_all('div', {'class': 'fact-stat'}):
        key = item.find('strong').get_text().strip()
        value = item.find('span').get_text().strip()
        data[key] = value

    # Specify the file name for the JSON file
    output_file = 'bu_facts_stats.json'

    # Write the extracted data to a JSON file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Data has been scraped and saved to '{output_file}'")
    
# Print the HTML content regardless of whether the facts_section is None or not
print(soup.prettify())



# 3 - Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.

# URL of the Wikipedia page with the list of US presidents
url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the table containing the list of presidents
    presidents_table = soup.find("table", class_="wikitable")

    # Initialize an empty list to store the data for each president
    presidents_data = []

    # Iterate over each row in the table (skipping the header row)
    for row in presidents_table.find_all("tr")[1:]:
        # Extract the data from the columns of the current row
        columns = row.find_all(["th", "td"])

        # Extract the president's number
        number = columns[0].get_text().strip()

        # Extract the president's name and lifespan
        name = columns[2].find("a").get_text().strip()
        lifespan = columns[2].find("span", {"style": "font-size:85%;"}).get_text().strip()

        # Extract the start and end dates of the presidency
        date_range = columns[3].get_text().strip().split("\u2013")
        start_date = date_range[0].strip()
        end_date = date_range[1].strip()

        # Extract the party affiliation and vice president(s) information
        party_info = columns[5].get_text().strip()
        if "[" in party_info:
            party_info = party_info[:party_info.index("[")]

        # Create a dictionary to store the data for the current president
        president_info = {
            "number": number,
            "name": name,
            "lifespan": lifespan,
            "start_date": start_date,
            "end_date": end_date,
            "party_info": party_info
        }

        # Append the dictionary to the list
        presidents_data.append(president_info)

    # Convert the list of dictionaries to JSON format
    presidents_json = json.dumps(presidents_data, indent=4)

    # Print the JSON data
    print(presidents_json)

    # You can also save the JSON data to a file if needed
    # with open("presidents.json", "w") as file:
    #     file.write(presidents_json)

else:
    print("Failed to retrieve the Wikipedia page.")




