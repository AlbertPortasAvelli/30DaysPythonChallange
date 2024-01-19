### Dictionaries ###
#A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# 1 - Creating a Dictionary
empty_dict = {}
person = {
    'first_name':'Albert',
    'last_name':'Portas',
    'age':30,
    'country':'Spain',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
# 2 - Dictionary Length
print(len(person))
# 3 - Accessing Dictionary Items
print(person['first_name'])
print(person['skills'][0])  
print(person['address']['street'])
print(person.get('first_name'))
# 4 - Adding Items to a Dictionary
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
# You can use extend() method if you want to add multiple values
# 5 - Modifying Items in a Dictionary
person['age'] = 252
print(person['age'])
# 6 - Checking Keys in a Dictionary
print('first_name' in person)
# 7 - Removing Key and Value Pairs from a Dictionary
person.pop('first_name')       
person.popitem()                
del person['is_married'] 
# 8 - Changing Dictionary to a List of Items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())     
# 9 - Clearing a Dictionary
print(dct.clear())
# 10 - Deleting a Dictionary
del dct
# 11 - Copy a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
# 12 - Getting Dictionary Keys as a List
keys = list(dct.keys())
print(keys)
# 13 - Getting Dictionary Values as a List
values = list(dct.values())
print(values)  