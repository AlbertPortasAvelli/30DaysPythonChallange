### Tuples ###
#A tuple is a collection of different data types which is ordered and unchangeable (immutable).

# 1 - Create a Tuple
new_tuple = ()
new_empty_tuple = tuple()
# 2 - Tuple length
len(new_tuple)
# 3 - Accessing Tuple Items
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
first_fruit = fruits[-4]
second_fruit = fruits[-3]
# 4 - Slicing tuples
all_fruits = fruits[0:4]
all_fruits= fruits[0:]
all_fruits = fruits[-4:]   
orange_mango = fruits[-3:-1]
# 5 - Changing Tuples to Lists
print(type(fruits))
fruits = list(fruits)
print(type(fruits))
fruits = tuple(fruits)
# 6 - Checking an Item in a Tuple
print('orange' in fruits)
print('apple' in fruits)
# 7 - Joining Tuples
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
# 8 - Deleting Tuples
del fruits