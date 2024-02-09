### Exercices ###

''' 1- Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
        - The min, max, mean, median, standard deviation of cats' weight in metric units.
        - The min, max, mean, median, standard deviation of cats' lifespan in years.
        - Create a frequency table of country and breed of cats
'''
import requests
import pandas as pd

# Define the API endpoint
cats_api = 'https://api.thecatapi.com/v1/breeds'

# Fetch data from the API
response = requests.get(cats_api)
data = response.json()

# Create a DataFrame from the API response
df = pd.DataFrame(data)

# Extract weight in metric units
df['weight_metric'] = df['weight'].apply(lambda x: x['metric'].split()[0] if x['metric'] else None)

# Convert weight to numeric
df['weight_metric'] = pd.to_numeric(df['weight_metric'], errors='coerce')

# Extract lifespan in years
df['lifespan_years'] = df['life_span'].apply(lambda x: x.split()[0] if x else None)

# Convert lifespan to numeric
df['lifespan_years'] = pd.to_numeric(df['lifespan_years'], errors='coerce')

# Calculate statistics for weight and lifespan
weight_stats = df['weight_metric'].describe()
lifespan_stats = df['lifespan_years'].describe()

# Create a frequency table of country and breed of cats
frequency_table = df.groupby(['origin', 'name']).size().reset_index(name='count')

print("Statistics for cats' weight in metric units:")
print(weight_stats)
print("\nStatistics for cats' lifespan in years:")
print(lifespan_stats)
print("\nFrequency table of country and breed of cats:")
print(frequency_table)