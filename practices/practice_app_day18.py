import re
from collections import Counter

def clean_text(text):
    cleaned_text = re.sub(r'[^A-Za-z\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    cleaned_text = cleaned_text.strip()
    return cleaned_text

def tokenize_text(text):
    return text.split()

def count_word_frequency(tokens):
    return Counter(tokens)

def find_top_words(word_counts, n=3):
    return word_counts.most_common(n)

def main():

    input_text = input("Enter your text: ")

    cleaned_text = clean_text(input_text)
    print("Cleaned Text:", cleaned_text)

    tokens = tokenize_text(cleaned_text)

    word_counts = count_word_frequency(tokens)

    top_words = find_top_words(word_counts)

    print("Three Most Frequent Words:")
    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
