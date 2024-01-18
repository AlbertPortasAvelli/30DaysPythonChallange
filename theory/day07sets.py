### Sets ###
#an unordered and mutable collection of unique elements.

# 1- Creating a Set
empty_set = set()
set_example =  {'banana', 'orange', 'mango', 'lemon'}
# 2 - Getting Set's Length
len(set_example)
# 3 - Accessing Items in a Set
#We use loops to access items. We will see this in loop section
# 4 - Checking an Item
print('There is a banana in the set') if 'banana' in set_example else None
# 5 - Adding Items to a Set
set_example.add('lime')
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
set_example.update(vegetables)
# 6 - Removing Items from a Set
set_example.remove('tomato')
set_example.pop()
removed_item = set_example.pop()
# 7 - Clearing Items in a Set
set_example.clear()
print(set_example)
# 8 - Deleting a Set
del empty_set
# 9 - Converting List to Set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits)
# 10 - Joining Sets
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables))
# 11 - Finding Intersection Items
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)
# 12 - Checking Subset and Super Set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers)
whole_numbers.issuperset(even_numbers)
# 13 - Checking the Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers)
# 14 - Finding Symmetric Difference Between Two Sets
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)
# 15 - Joining Sets
odd_numbers = set()
even_numbers = {0, 2, 4 ,6, 8}
even_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers)
