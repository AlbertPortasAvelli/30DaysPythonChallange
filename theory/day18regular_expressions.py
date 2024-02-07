### Regular Expressions ###
# sequences of characters that define a search pattern.

#Methods in re Module
import re

# - re.search(pattern, string, flags=0)
#This method searches for the first occurrence of a pattern within a string.


text = "The cat sat on the mat"
pattern = "cat"
match = re.search(pattern, text)
if match:
    print("Pattern found at index:", match.start())
# - re.match(pattern, string, flags=0):
#This method checks for a match only at the beginning of the string.


text = "The cat sat on the mat"
pattern = "The"
match = re.match(pattern, text)
if match:
    print("Pattern found at index:", match.start())
# - re.findall(pattern, string, flags=0):
#This method finds all occurrences of a pattern in a string and returns them as a list.


text = "The cat sat on the mat"
pattern = "at"
matches = re.findall(pattern, text)
print("Occurrences of 'at':", matches)
# - re.sub(pattern, replacement, string, count=0, flags=0):
#This method replaces all occurrences of a pattern in a string with a replacement string.


text = "The cat sat on the mat"
pattern = "cat"
replacement = "dog"
new_text = re.sub(pattern, replacement, text)
print("New text:", new_text)
# - re.compile(pattern, flags=0):
#This method compiles a regular expression pattern into a regular expression object, which can then be used for matching.


pattern = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', re.IGNORECASE)
text = "Emails: john.doe@example.com, alice_123@example.net"
matches = pattern.findall(text)
print("Emails found:", matches)
# - Replacing a Substring
text = "The cat sat on the mat"
pattern = "cat"
replacement = "dog"

new_text = re.sub(pattern, replacement, text)
print("New text:", new_text)
# 1 - Splitting Text Using RegEx Split

text = "The cat sat on the mat"
pattern = r"\s"  

split_text = re.split(pattern, text)
print("Split text:", split_text)
'''
2 - Writing RegEx Patterns
    []: A set of characters
        - [a-c] means, a or b or c
        - [a-z] means, any letter from a to z
        - [A-Z] means, any character from A to Z
        - [0-3] means, 0 or 1 or 2 or 3
        - [0-9] means any number from 0 to 9
        - [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9

    ****: Used to escape special characters
        - \: uses to escape special characters

        - \d: Matches any digit character (0-9)
        - \d means: match where the string contains digits (numbers from 0-9)

        - \D: Matches any non-digit character
        - \D means: match where the string does not contain digits

        - .: Matches any character except newline character (\n)
        - . : any character except new line character(\n)

        - ^: Matches the start of the string
        - ^: starts with
        - r'^substring' e.g., r'^love', a sentence that starts with a word love

        - [^]: Matches any character not listed within the brackets
        - r'[^abc] means not a, not b, not c.

        - $: Matches the end of the string
        - $: ends with
        - r'substring$' e.g., r'love$', a sentence that ends with a word love

        - *: Matches zero or more occurrences of the preceding character
        - *: zero or more times
        - r'[a]*' means a optional or it can occur many times.

        - +: Matches one or more occurrences of the preceding character
        - +: one or more times
        - r'[a]+' means at least once (or more)

        - ?: Matches zero or one occurrence of the preceding character
        - ?: zero or one time
        - r'[a]?' means zero times or once

        - {n}: Matches exactly n occurrences of the preceding character
        - {3}: Exactly 3 characters

        - {n,}: Matches at least n occurrences of the preceding character
        - {3,}: At least 3 characters

        - {n,m}: Matches from n to m occurrences of the preceding character
        - {3,8}: 3 to 8 characters

        - |: Matches either the pattern before or after the operator
        - |: Either or
        - r'apple|banana' means either apple or banana

        - (): Groups expressions together and captures matched substrings
        - (): Capture and group
'''

# 3 - Square Bracket
regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)

# 4 - Escape character(\) in RegEx
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

# 5 - One or more times(+)
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!

# 6 - Period(.)
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

# 7 - Zero or more times(*)
regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

# 8 - Zero or one time(?)
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

# 9 - Quantifier in RegEx

text = "aa, aaaa, aaaaaa"
pattern = r'a{2,4}'
matches = re.findall(pattern, text)
print(matches)  # Output: ['aa', 'aaaa']

# 10 - Cart ^
#       - Starts with
text = "apple banana cherry"
pattern = r"^apple"
match = re.search(pattern, text)
if match:
    print("Pattern found at index:", match.start())
#       - Negation
text = "apple banana cherry"
pattern = r"[^a]"
matches = re.findall(pattern, text)
print("Matches:", matches)
