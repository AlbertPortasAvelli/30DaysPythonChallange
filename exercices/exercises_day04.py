### Exercices Day 4 ###

# 1 - Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a, b, c, d = 'Thirty', 'Days', 'Of', 'Python'
challenge = ' '.join([a, b, c, d])
print(challenge)
# 2 - Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
a, b, c = "Coding", 'For', 'All'
total = f'{a} {b} {c}'
print(total)
# 3 - Declare a variable named company and assign it to an initial value "Coding For All".
company = total
# 4 - Print the variable company using print().
print(company)
# 5 - Print the length of the company string using len() method and print().
print(len(company))
# 6 - Change all the characters to uppercase letters using upper() method.
print(company.upper())
# 7 - Change all the characters to lowercase letters using lower() method.
print(company.lower())
# 8 - Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
a, b, c = company[0:5], company[7:10], company[11:14]
print(f'{a.capitalize()} {b.capitalize()} {c.capitalize()}')
print(f'{company.title()}')
indices_to_swap = [-1, 6, 10]
swapped_characters = [char.swapcase() if i in indices_to_swap else char for i, char in enumerate(company)]
result_string = ''.join(swapped_characters)
print(result_string)
# 9 - Cut(slice) out the first word of Coding For All string.
cut_string = company.split(' ', 1)[1]
print(cut_string)
# 10 - Check if Coding For All string contains a word Coding using the method index, find or other methods.
search_word = 'Coding'
try:
    # Using index() to find the index of the search word
    index = company.index(search_word)
    print(f'The word "{search_word}" is present at index {index}.')
except ValueError:
    print(f'The word "{search_word}" is not found in the string.')
# 11 - Replace the word coding in the string 'Coding For All' to Python.
new_string = company.replace('Coding', 'Python')
print(new_string)
# 12 - Change Python for All to Python for Everyone using the replace method or other methods.
change = new_string.replace('All', 'Everyone')
print(change)
# 13 - Split the string 'Coding For All' using space as the separator (split()) .
original = 'Coding For All'
seperated_words = original.split(' ')
print(seperated_words)
# 14 - "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
seperated_companies = companies.split(',')
print(seperated_companies)
# 15 - What is the character at index 0 in the string Coding For All.
print(original[0])
# 16 - What is the last index of the string Coding For All.
print(original[len(original) - 1 ])
# 17 - What character is at index 10 in "Coding For All" string.
print(original[10])
# 18 - Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = 'Python For Everyone'
acronym = ''.join(word[0] for word in phrase.split())
print(acronym)
# 19 - Create an acronym or an abbreviation for the name 'Coding For All'.
acronym_original = ''.join(word[0] for word in original.split())
print(acronym_original)
# 20 - Use index to determine the position of the first occurrence of C in Coding For All.
try:
    # Using index() to find the position of the character
    position = original.index('C')
    print(f'The first occurrence of "C" is at position {position}.')
except ValueError:
    print(f'The character "C" is not found in the string.')
# 21 - Use index to determine the position of the first occurrence of F in Coding For All.
try:
    # Using index() to find the position of the character
    position = original.index('F')
    print(f'The first occurrence of "F" is at position {position}.')
except ValueError:
    print(f'The character "F" is not found in the string.')
# 22 - Use rfind to determine the position of the last occurrence of l in Coding For All People.
position = original.rfind('l')
if position != -1:
    print(f'The last occurrence of "l" is at position {position}.')
else:
    print(f'The character "l" is not found in the string.')
# 23 - Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
search_word = 'because'
try:
    position = sentence.index(search_word)
    print(f'The first occurrence of "{search_word}" starts at position {position}.')
except ValueError:
    print(f'The word "{search_word}" is not found in the sentence.')
position = sentence.find(search_word)
if position != -1:
    print(f'The first occurrence of "{search_word}" starts at position {position}.')
else:
    print(f'The word "{search_word}" is not found in the sentence.')
# 24 - Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
try:
    # Using rindex() to find the position of the last occurrence of the word
    position = sentence.rindex(search_word)
    print(f'The last occurrence of "{search_word}" starts at position {position}.')
except ValueError:
    print(f'The word "{search_word}" is not found in the sentence.')
# 25 - Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start_position = sentence.find('because')
end_position = sentence.rfind('because') + len('because')
sliced_phrase = sentence[start_position:end_position]
print(sliced_phrase)
# 26 - Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
try:
    # Using index() to find the position of the word
    position = sentence.index(search_word)
    print(f'The first occurrence of "{search_word}" starts at position {position}.')
except ValueError:
    print(f'The word "{search_word}" is not found in the sentence.')
# 27 - Does 'Coding For All' start with a substring Coding?
substring = 'Coding'
if original.startswith(substring):
    print(f'The string starts with "{substring}".')
else:
    print(f'The string does not start with "{substring}".')
# 28 - Does 'Coding For All' end with a substring coding?
substring = 'coding'
if original.endswith(substring):
    print(f'The string ends with "{substring}".')
else:
    print(f'The string does not end with "{substring}".')
# 29 - '   Coding For All      '  , remove the left and right trailing spaces in the given string.
original_string = '   Coding For All      '
trimmed_string = original_string.strip()
print(trimmed_string)
# 30 - Which one of the following variables return True when we use the method isidentifier():
#       - 30DaysOfPython
#       - thirty_days_of_python
variable1 = "30DaysOfPython"
variable2 = "thirty_days_of_python"
is_identifier_var1 = variable1.isidentifier()
is_identifier_var2 = variable2.isidentifier()
print(f'Is "{variable1}" a valid identifier? {is_identifier_var1}')
print(f'Is "{variable2}" a valid identifier? {is_identifier_var2}')
# 31 - The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_string = '# '.join(libraries)
print(joined_string)
# 32 - Use the new line escape sequence to separate the following sentences.
#       - I am enjoying this challenge.
#       - I just wonder what is next.
sentence1 = 'I am enjoying this challenge.'
sentence2 = 'I just wonder what is next.'
combined_sentences = sentence1 + '\n' + sentence2
print(combined_sentences)
# 33 - Use a tab escape sequence to write the following lines.
#       - Name      Age     Country   City
#       - Asabeneh  250     Finland   Helsinki
header = 'Name\tAge\tCountry\tCity'
data = 'Asabeneh\t250\tFinland\tHelsinki'
table = header + '\n' + data
print(table)
# 34 - Use the string formatting method to display the following:
#        - radius = 10
#        - area = 3.14 * radius ** 2
#        - The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
output = f'The area of a circle with radius {radius} is {area} square meters.'
print(output)
# 35 - Make the following using string formatting methods:
#       - 8 + 6 = 14
#       - 8 - 6 = 2
#       - 8 * 6 = 48
#       - 8 / 6 = 1.33
#       - 8 % 6 = 2
#       - 8 // 6 = 1
#       - 8 ** 6 = 262144
addition = 8 + 6
subtraction = 8 - 6
multiplication = 8 * 6
division = 8 / 6
modulo = 8 % 6
floor_division = 8 // 6
exponentiation = 8 ** 6
print("{} + {} = {}".format(8, 6, addition))
print("{} - {} = {}".format(8, 6, subtraction))
print("{} * {} = {}".format(8, 6, multiplication))
print("{} / {} = {:.2f}".format(8, 6, division))
print("{} % {} = {}".format(8, 6, modulo))
print("{} // {} = {}".format(8, 6, floor_division))
print("{} ** {} = {}".format(8, 6, exponentiation))