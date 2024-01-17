### Exercices Day 6 ###

# 1 - Create an empty tuple
empty_tuple = tuple()
# 2 - Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('David', 'Charles')
sisters = ('Abby', 'Mery')
# 3 - Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
# 4 - How many siblings do you have?
# I have 2 siblings
# 5 - Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father_and_mother = ('John', 'Mary')
family_members = siblings + father_and_mother
# Exercices Level 2
# 1 - Unpack siblings and parents from family_members
(*siblings, father, mother) = family_members
# 2 - Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'spinach', 'broccoli')
animal_products = ('beef', 'eggs', 'cheese')
food_stuff_tp = fruits + vegetables + animal_products
# 3 - Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# 4 - Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_tp) // 2
middle_item_or_items = food_stuff_tp[middle_index] if len(food_stuff_tp) % 2 != 0 else food_stuff_tp[middle_index - 1:middle_index + 1]
# 5 - Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
# 6 - Delete the food_staff_tp tuple completely
del food_stuff_tp
# 7 - Check if an item exists in tuple:
#       - Check if 'Estonia' is a nordic country
#       - Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
estonia_is_nordic = 'Estonia' in nordic_countries
iceland_is_nordic = 'Iceland' in nordic_countries
print('Is Estonia a Nordic country?', estonia_is_nordic)
print('Is Iceland a Nordic country?', iceland_is_nordic)