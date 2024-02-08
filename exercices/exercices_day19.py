### Exercices ###

# 1 - Write a function which count number of lines and number of words in a 
#text. All the files are in the data the folder: 
#a) Read obama_speech.txt file and count number of lines and words 
#b) Read michelle_obama_speech.txt file and count number of lines and words
#c) Read donald_speech.txt file and count number of lines and words 
#d) Read melina_trump_speech.txt file and count number of lines and words

def count_lines_and_words(file_name):
    base_dir = r'C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\exercices\\data\\' 
    file_path = base_dir + file_name  
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            return num_lines, num_words
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None, None
    except IOError:
        print(f"Error reading file '{file_path}'.")
        return None, None

file_names = [
    'obama_speech.txt',
    'michelle_obama_speech.txt',
    'donald_speech.txt',
    'melina_trump_speech.txt'
]

for file_name in file_names:
    num_lines, num_words = count_lines_and_words(file_name)
    if num_lines is not None and num_words is not None:
        print(f"File: {file_name}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print()

# 2 - Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def most_spoken_languages(filename, n):
    try:
        with open(filename, 'r', encoding='utf-8') as file:  # Specify encoding as 'utf-8'
            # Read the entire file as text
            file_contents = file.read()

            # Extract the list of countries data from the Python file
            countries_data = eval(file_contents)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading file '{filename}': {e}")
        return None

    # Proceed with the rest of the logic to find the most spoken languages
    language_counts = {}
    for country in countries_data:
        for language in country['languages']:
            language_counts[language] = language_counts.get(language, 0) + 1

    sorted_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:n]

# Example usage
base_dir = 'C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\exercices\\data\\'
print(most_spoken_languages(filename= base_dir + 'countries-data.py' , n=10))
print(most_spoken_languages(filename= base_dir + 'countries-data.py', n=3))

# 3 - Read the countries_data.py data file in data directory, create a function that creates a list of the ten most populated countries
def most_populated_countries(filename, n):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file_contents = file.read()

            countries_data = eval(file_contents)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading file '{filename}': {e}")
        return None

    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return [(country['name'], country['population']) for country in sorted_countries[:n]]

base_dir = 'C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\exercices\\data\\'
most_populated = most_populated_countries(filename= base_dir + 'countries-data.py' , n=10)
if most_populated:
    print("Ten most populated countries:")
    for idx, (name, population) in enumerate(most_populated, 1):
        print(f"{idx}. {name}: {population}")
else:
    print("An error occurred while processing the data.")

#=============================================================================
#Level 2
#=============================================================================

# 4 - Extract all incoming email addresses as a list from the email_exchange_big.txt file.

import re

def extract_email_addresses(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

            email_addresses = re.findall(pattern, text)

            return email_addresses
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_path = 'C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\exercices\\data\\email_exchanges_big.txt'
email_addresses = extract_email_addresses(file_path)
if email_addresses:
    print("Extracted email addresses:")
    for email in email_addresses:
        print(email)
else:
    print("An error occurred while processing the file.")

# 5 - Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
# 6 - Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
import nltk
from collections import Counter

def find_most_common_words(input_data, n):
    nltk.download('punkt')
    nltk.download('stopwords')
    from nltk.corpus import stopwords

    # If input_data is a file path, read the file
    if isinstance(input_data, str) and input_data.endswith('.txt'):
        with open(input_data, 'r') as file:
            text = file.read().lower()
    else:
        text = input_data.lower()

    # Tokenize the text and filter out stopwords
    words = nltk.word_tokenize(text)
    english_stopwords = set(stopwords.words('english'))
    words = [word for word in words if word.isalpha() and word not in english_stopwords]

    # Count occurrences of each word
    word_counts = Counter(words)

    # Get the n most common words
    most_common_words = word_counts.most_common(n)

    return most_common_words

# Speech file paths
speech_files = {
    'Obama': 'C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\exercices\\data\\obama_speech.txt',
    'Michelle': 'C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\exercices\\data\\michelle_obama_speech.txt',
    'Trump': 'C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\exercices\\data\\donald_speech.txt',
    'Melina': 'C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\exercices\\data\\melina_trump_speech.txt'
}

for speaker, file_path in speech_files.items():
    print(f"Ten most frequent words used in {speaker}'s speech:")
    most_common_words = find_most_common_words(file_path, 10)
    for idx, (word, count) in enumerate(most_common_words, 1):
        print(f"{idx}. {word}: {count}")
    print()

# 7 - Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
    
import string
from collections import Counter
import math

def clean_text(text):
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    text = text.lower()
    return text

def remove_stopwords(text, stopwords):
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)

def check_text_similarity(text1, text2):
    clean_text1 = clean_text(text1)
    clean_text2 = clean_text(text2)

    words1 = clean_text1.split()
    words2 = clean_text2.split()

    word_freq1 = Counter(words1)
    word_freq2 = Counter(words2)

    dot_product = sum(word_freq1[word] * word_freq2[word] for word in word_freq1 if word in word_freq2)

    magnitude1 = math.sqrt(sum(word_freq1[word] ** 2 for word in word_freq1))
    magnitude2 = math.sqrt(sum(word_freq2[word] ** 2 for word in word_freq2))

    similarity = dot_product / (magnitude1 * magnitude2)

    return similarity

def load_stopwords(file_path):
    with open(file_path, 'r') as file:
        stopwords = file.read().splitlines()
    return stopwords

def main():
    
    stopwords = load_stopwords('C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\exercices\\data\\stop_words.py')

    with open('C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\exercices\\data\\michelle_obama_speech.txt', 'r') as file:
        michelle_text = file.read()
    with open('C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\exercices\\data\\melina_trump_speech.txt', 'r') as file:
        melina_text = file.read()

    cleaned_michelle_text = remove_stopwords(clean_text(michelle_text), stopwords)
    cleaned_melina_text = remove_stopwords(clean_text(melina_text), stopwords)

    similarity = check_text_similarity(cleaned_michelle_text, cleaned_melina_text)
    print(f"Similarity between Michelle's and Melina's speech: {similarity}")

if __name__ == "__main__":
    main()

# 8 - Find the 10 most repeated words in the romeo_and_juliet.txt

def find_most_repeated_words(file_path, n):
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower() 

            
            words = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in text).split()

            
            word_counts = Counter(words)

          
            most_repeated_words = word_counts.most_common(n)

            return most_repeated_words
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_path = 'C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\exercices\\data\\romeo_and_juliet.txt'  
most_repeated_words = find_most_repeated_words(file_path, 10)
if most_repeated_words:
    print("10 most repeated words in 'romeo_and_juliet.txt':")
    for idx, (word, count) in enumerate(most_repeated_words, 1):
        print(f"{idx}. {word}: {count}")
else:
    print("An error occurred while processing the file.")

# 9 - Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript
import csv

def count_lines_with_keywords(file_path, keyword_list):
    python_count = 0
    javascript_count = 0
    java_count = 0
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if any(keyword.lower() in row[1].lower() for keyword in keyword_list):
                if 'python' in row[1].lower():
                    python_count += 1
                if 'javascript' in row[1].lower():
                    javascript_count += 1
                if 'java' in row[1].lower() and 'javascript' not in row[1].lower():
                    java_count += 1
    return python_count, javascript_count, java_count

file_path = 'C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\exercices\\data\\hacker_news.csv'

keyword_list_python = ['python']
keyword_list_javascript = ['javascript']
keyword_list_java = ['java']

python_count, _, _ = count_lines_with_keywords(file_path, keyword_list_python)
print(f"Number of lines containing 'python' or 'Python': {python_count}")

_, javascript_count, _ = count_lines_with_keywords(file_path, keyword_list_javascript)
print(f"Number of lines containing 'JavaScript', 'javascript', or 'Javascript': {javascript_count}")

_, _, java_count = count_lines_with_keywords(file_path, keyword_list_java)
print(f"Number of lines containing 'Java' and not 'JavaScript': {java_count}")