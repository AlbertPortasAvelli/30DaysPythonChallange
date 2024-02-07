from collections import Counter
import re
### Exercices ###

# 1 - What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\b\w+\b', paragraph.lower())

word_counts = Counter(words)

sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

print(sorted_word_counts)
# 2 - The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

text = "# 2 - The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

numbers = [int(num) for num in re.findall(r'-?\d+', text)]

sorted_numbers = sorted(numbers)

distance = sorted_numbers[-1] - sorted_numbers[0]

print("Distance between the two furthest particles:", distance)

#============================================================================
#Level 2
#============================================================================

# 1 - Write a pattern which identifies if a string is a valid python variable
def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_]\w*$'
    return re.match(pattern, variable) is not None

print(is_valid_variable('first_name'))   # True
print(is_valid_variable('first-name'))   # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))    # True

#=============================================================================
#Level 3
#=============================================================================

# 1 - Clean the following text. After cleaning, count three most frequent words in the string.

def clean_text(text):

    cleaned_text = re.sub(r'[^A-Za-z\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    cleaned_text = cleaned_text.strip()
    return cleaned_text

def most_frequent_words(text, n=3):

    words = text.split()

    word_counts = Counter(words)

    top_n_words = word_counts.most_common(n)
    return top_n_words

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)

print(most_frequent_words(cleaned_text))