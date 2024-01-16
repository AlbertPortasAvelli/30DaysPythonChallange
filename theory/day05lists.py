### LISTS ###

#is collection of different data types which is ordered and modifiable(mutable).

# 1 - Create a List
fruit_list = list()
food_list = []
vegetables = ['carrot', 'onion', 'lettuce']
user_info = ['Albert', 'Portas', 1.84, 30, {'country' : 'Spain', 'city': 'Girona'}]
# 2 - Accessing List Items Using Negative Indexing
#   Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.
print(user_info[-1])
print(user_info[-2])
# 3 - Unpacking List Items
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
# 4 - Slicing Items from a List
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
#   5 - Modifying Lists
fruits[0] = 'strawberry'
print(fruits)
#   6 - Checking Items in a List
exist = 'banana' in fruits
print(exist)
#   7 - Adding Items to a List
fruits.append('banana')
print(fruits)
#   8 - Inserting Items into a List
fruits.insert(3, 'blueberry')
print(fruits)
#   9 - Removing Items from a List
fruits.remove('blueberry')
print(fruits)
#   10 - Removing Items Using Pop
fruits.pop()
print(fruits)
fruits.pop(3)
print(fruits)
#   11 - Removing Items Using Del
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined
#   12 - Clearing List Items
fruits.clear()
print(fruits)
#   13 - Copying a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
#   14 - Joining Lists
fruits_and_vegetebales = fruits + vegetables
print(fruits_and_vegetebales)

num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
#   15 - Counting Items in a List
print(fruits.count('orange'))
#   16 - Finding Index of an Item
print(fruits.index('orange'))
#   17 - Reversing a List
print(fruits)
print(fruits.reverse)
#   18 - Sorting List Items
print(fruits.sort())#ascending
print(fruits.sort(reverse=True))#descending
print(sorted(fruits))#returns the ordered list without modifying the original list