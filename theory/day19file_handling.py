### File Handling ###

# 1 - Opening Files for Reading

file_path = 'example.txt'  # Replace 'example.txt' with the path to your file
try:
    with open(file_path, 'r') as file:
        file_contents = file.read()
        print(file_contents)
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An error occurred while reading the file.")

# 1.1 - readline()
file_path = 'example.txt'  
try:
    with open(file_path, 'r') as file:
        # Read the first line of the file
        first_line = file.readline()
        print("First line:", first_line)
        
        # Read the second line of the file
        second_line = file.readline()
        print("Second line:", second_line)
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An error occurred while reading the file.")
# 1.2 - readlines()
#   read all lines from a file and return them as a list of strings.
file_path = 'example.txt' 
try:
    with open(file_path, 'r') as file:
        
        lines = file.readlines()
        
        for line in lines:
            print(line.strip())  # strip() is used to remove trailing newline characters
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An error occurred while reading the file.")
# 1.3 - splitlines()
#It is similar to split('\n'), but it also handles various line endings such as \r, \n, and \r\n.

file_path = 'example.txt'  
try:
    with open(file_path, 'r') as file:
   
        file_contents = file.read()
    
        lines = file_contents.splitlines()
    
        for line in lines:
            print(line)
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An error occurred while reading the file.")

# 2 -  Opening Files for Writing and Updating

# 2.1 - Writing
file_path = 'example.txt' 
try:
    with open(file_path, 'w') as file:
        file.write("Hello, world!\n")
        file.write("This is a new line.")
except IOError:
    print("An error occurred while writing to the file.")
# 2.2 - Appending
    file_path = 'example.txt'  
try:
    with open(file_path, 'a') as file:
        file.write("This line will be appended.\n")
except IOError:
    print("An error occurred while appending to the file.")
# 2.3 - Updating
    file_path = 'example.txt'  
try:
    with open(file_path, 'r+') as file:
        content = file.read()
        
        modified_content = content + "\nThis line is added in update mode."
        # Move the file cursor to the beginning of the file
        file.seek(0)
        # Write the modified content back to the file
        file.write(modified_content)
except IOError:
    print("An error occurred while updating the file.")
# 3 - Deleting Files
    import os

file_path = 'example.txt' 
try:
    os.remove(file_path)
    print("File deleted successfully.")
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to delete the file.")
except OSError as e:
    print(f"An error occurred: {e}")
# 4 - File Types
    
# 4.1 - File with txt Extension
# It is the same examples as the once i did already.

# 4.2 - File with json Extension
# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

# 4.3 - Changing JSON to Dictionary

import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# 4.4 - hanging Dictionary to JSON
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

# 4.5 - Saving as JSON File
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
# 5 - File with csv Extension
import csv

file_path = './files/csv_example.csv' 

# Read the CSV file
try:
    with open(file_path, newline='') as f:
        csv_reader = csv.reader(f, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are: {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} is a teacher. He lives in {row[1]}, {row[2]}.')
                line_count += 1
        print(f'Number of lines: {line_count}')
except FileNotFoundError:
    print("The CSV file does not exist.")
except PermissionError:
    print("You do not have permission to read the CSV file.")
except Exception as e:
    print(f"An error occurred while reading the CSV file: {e}")

# Delete the CSV file
try:
    os.remove(file_path)
    print("CSV file deleted successfully.")
except FileNotFoundError:
    print("The CSV file does not exist.")
except PermissionError:
    print("You do not have permission to delete the CSV file.")
except Exception as e:
    print(f"An error occurred while deleting the CSV file: {e}")

# 6 - File with xlsx Extension
import xlrd

file_path = './files/excel_example.xlsx'  
# Read the Excel file
try:
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)
    for row_index in range(sheet.nrows):
        row = sheet.row_values(row_index)
        print(row)
except FileNotFoundError:
    print("The Excel file does not exist.")
except Exception as e:
    print(f"An error occurred while reading the Excel file: {e}")

# Delete the Excel file
try:
    os.remove(file_path)
    print("Excel file deleted successfully.")
except FileNotFoundError:
    print("The Excel file does not exist.")
except PermissionError:
    print("You do not have permission to delete the Excel file.")
except Exception as e:
    print(f"An error occurred while deleting the Excel file: {e}")

# 7 - File with xml Extension
import xml.etree.ElementTree as ET

file_path = './files/xml_example.xml'  

# Read the XML file
try:
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Example: Print all elements and their text
    for elem in root.iter():
        print(f"{elem.tag}: {elem.text}")
except FileNotFoundError:
    print("The XML file does not exist.")
except ET.ParseError:
    print("Invalid XML file format.")
except Exception as e:
    print(f"An error occurred while reading the XML file: {e}")

# Delete the XML file
try:
    os.remove(file_path)
    print("XML file deleted successfully.")
except FileNotFoundError:
    print("The XML file does not exist.")
except PermissionError:
    print("You do not have permission to delete the XML file.")
except Exception as e:
    print(f"An error occurred while deleting the XML file: {e}")