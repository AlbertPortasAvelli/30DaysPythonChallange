import re
import sys
import time

def read_countries_data(file_path):
    """Reads data from the specified Python file and returns the list of dictionaries."""
    with open(file_path, 'r', encoding='utf-8') as file:
        python_code = file.read()

    match = re.search(r'\[.*\]', python_code, re.DOTALL)
    if match:
        countries_data_str = match.group(0)
        try:
            countries_data = eval(countries_data_str)
            return countries_data
        except SyntaxError:
            print("Error: Unable to evaluate the list of dictionaries.")
    else:
        print("List of dictionaries not found in the Python file.")
        return None


def display_country_info(country_info):
    """Displays detailed information about a country."""
    print("\nDisplaying Country Information:")
    try:
        name = country_info.get('name', 'N/A').encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
        capital = country_info.get('capital', 'N/A').encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
        population = country_info.get('population', 'N/A')
        languages = ', '.join(country_info.get('languages', []))
        currency = country_info.get('currency', 'N/A').encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
        flag = country_info.get('flag', 'N/A').encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)

        print(f"Country: {name}")
        print(f"Capital: {capital}")
        print(f"Population: {population}")
        print(f"Languages: {languages if languages else 'N/A'}")
        print(f"Currency: {currency}")
        print(f"Flag: {flag}\n")

        # Add a brief pause to allow time to read the information
        time.sleep(3)

    except Exception as e:
        print(f"Error displaying country information: {e}")


def main():
    file_path = r'c:\Users\alber\Documents\DocumentsAlbert\CV\Linkedin projects\30daysPython\exercices\someinfo_needed\countries-data.py'
    countries_data = read_countries_data(file_path)

    if countries_data:
        print("Welcome to the Country Information App!")

        while True:
            print("\nSelect a country to get detailed information:")
            for index, country_info in enumerate(countries_data, start=1):
                print(f"{index}. {country_info['name']}")

            print("0. Exit")

            try:
                choice = input("Enter your choice: ")
                if choice == '0':
                    print("Exiting the Country Information App. Goodbye!")
                    break

                choice = int(choice)
                if 1 <= choice <= len(countries_data):
                    selected_country = countries_data[choice - 1]
                    display_country_info(selected_country)

                else:
                    print("Invalid choice. Please enter a valid number.")

            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()