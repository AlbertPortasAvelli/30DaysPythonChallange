### Exercices ###

# 1 - Create an empty dictionary called dog
dog = {}
# 2 - Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Nuca'
dog['color'] = 'Black'
dog['breed'] = 'Belgian Malinois'
dog['legs'] = 4
dog['age'] = 12
# 3 - Create a student dictionary and add first_name, last_name,
# gender, age, marital status, skills, country, city and address as keys for 
# the dictionary
student = {}
student['first_name'] = 'John'
student['last_name'] = 'Doe'
student['gender'] = 'Male'
student['age'] = 20
student['marital_status'] = 'Single'
student['skills'] = ['Programming', 'Data Analysis']
student['country'] = 'United States'
student['city'] = 'New York'
student['address'] = '123 Main Street'
# 4 - Get the length of the student dictionary
print(len(student))
# 5 - Get the value of skills and check the data type, it should be a list
skills_value = student.get('skills')
skills_data_type = type(skills_value)
print("Skills:", skills_value)
print("Data Type of Skills:", skills_data_type)
# 6 - Modify the skills values by adding one or two skills
student['skills'].extend(['Communication', 'Problem Solving'])
# 7 - Get the dictionary keys as a list
student_keys = list(student.keys())
# 8 - Get the dictionary values as a list
student_values = list(student.values())
# 9 - Change the dictionary to a list of tuples using items() method
student_tuples = list(student.items())
# 10 - Delete one of the items in the dictionary
removed_item = student.popitem()
print("Removed Item:", removed_item)
# 11 - Delete one of the dictionaries
del student