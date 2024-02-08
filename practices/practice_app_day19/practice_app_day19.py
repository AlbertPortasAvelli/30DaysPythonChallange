import csv
import json

def create_csv_file(file_name, data):
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Age', 'Country'])  # Write header
            for item in data:
                writer.writerow([item['name'], item['age'], item['country']])
        print(f"CSV file '{file_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the CSV file: {e}")

def create_json_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"JSON file '{file_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the JSON file: {e}")

def create_txt_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            for item in data:
                file.write(f"Name: {item['name']}, Age: {item['age']}, Country: {item['country']}\n")
        print(f"TXT file '{file_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the TXT file: {e}")

def get_user_data():
    data = []
    while True:
        name = input("Enter name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        age = input("Enter age: ")
        country = input("Enter country: ")
        data.append({'name': name, 'age': age, 'country': country})
    return data

def choose_file_format():
    while True:
        file_format = input("Choose file format (csv/json/txt): ")
        if file_format.lower() in ['csv', 'json', 'txt']:
            return file_format.lower()
        else:
            print("Invalid file format. Please choose 'csv', 'json', or 'txt'.")

def main():
    data = get_user_data()
    file_format = choose_file_format()
    file_name = input("Enter file name: ")
    if file_format == 'csv':
        create_csv_file(file_name, data)
    elif file_format == 'json':
        create_json_file(file_name, data)
    elif file_format == 'txt':
        create_txt_file(file_name, data)

if __name__ == "__main__":
    main()