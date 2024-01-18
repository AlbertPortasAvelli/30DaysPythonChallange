### Exercices ###

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1 - Find the length of the set it_companies
print(f'Length : {len(it_companies)}')
# 2 - Add 'Twitter' to it_companies
it_companies.add('Twitter')
# 3 - Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Netflix', 'Samsung'])
# 4 - Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
# 5 - What is the difference between remove and discard
#   The discard() Does not raise any error if the element is not found. 
#It silently continues if the element is not present.

#============================================================================
# LEVEL 2
#============================================================================

# 1 - Join A and B
A_and_B = A.union(B)
# 2 - Find A intersection B
print(A.intersection(B))
# 3 - Is A subset of B
is_subset_method = A.issubset(B)
is_subset_operator = A <= B
# 4 - Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets using isdisjoint():", are_disjoint)
# 5 - Join A with B and B with A
A_union_B = A.union(B)
B_union_A = B.union(A)
# 6 - What is the symmetric difference between A and B
symmetric_difference_result = A.symmetric_difference(B)
symmetric_difference_operator = A ^ B
# 7 - Delete the sets completely
del it_companies, A, B

#==========================================================================
#LEVEL 3
#==========================================================================

# 1 - Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
list_length = len(age)
set_length = len(age_set)
print(f"Length of the list: {list_length}")
print(f"Length of the set: {set_length}")
if list_length > set_length:
    print("The length of the list is greater.")
elif set_length > list_length:
    print("The length of the set is greater.")
else:
    print("The length of the list and set are equal.")
# 2 - Explain the difference between the following data types: string, list, tuple and set
    '''
    String:

        - A string is a sequence of characters.
        - It is immutable, meaning you cannot modify its individual elements once it is created.
        - It is enclosed in single (' '), double (" "), or triple (''' ''' or """ """) quotes.
        - Common string operations include indexing, slicing, concatenation, and various string methods.
    List:

        - A list is an ordered and mutable collection of elements.
        - Elements in a list can be of different data types.
        - Lists are created using square brackets [].
        - You can modify, add, and remove elements from a list.
    Tuple:

        - A tuple is an ordered and immutable collection of elements.
        - Tuples are created using parentheses ().
        - Like lists, elements in a tuple can be of different data types.
        - Once a tuple is created, you cannot modify its elements.
    Set:

        -  A set is an unordered and mutable collection of unique elements.
        - Sets are created using curly braces {} or the set() constructor.
        - Sets do not allow duplicate elements, and they are useful for operations like union, intersection, difference, and testing membership.
    '''
# 3 - I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))