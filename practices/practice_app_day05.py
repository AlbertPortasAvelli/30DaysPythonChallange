# Shopping List Application

# Initialize an empty shopping list
shopping_list = []

# Function to display the shopping list
def display_list():
    print("Shopping List:")
    for item in shopping_list:
        print(f"- {item}")
    print(f"Total items: {len(shopping_list)}\n")

# Function to add an item to the shopping list
def add_item(item):
    shopping_list.append(item)
    print(f"{item} added to the shopping list.\n")

# Function to remove an item from the shopping list
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.\n")
    else:
        print(f"{item} is not in the shopping list.\n")

# Function to check if an item is in the shopping list
def check_item(item):
    if item in shopping_list:
        print(f"Yes, {item} is in the shopping list.\n")
    else:
        print(f"No, {item} is not in the shopping list.\n")

# Function to clear the entire shopping list
def clear_list():
    shopping_list.clear()
    print("Shopping list cleared.\n")

# Main loop
while True:
    print("Choose an option:")
    print("1. View Shopping List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Check Item")
    print("5. Clear Shopping List")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        display_list()
    elif choice == '2':
        item_to_add = input("Enter the item to add: ")
        add_item(item_to_add)
    elif choice == '3':
        item_to_remove = input("Enter the item to remove: ")
        remove_item(item_to_remove)
    elif choice == '4':
        item_to_check = input("Enter the item to check: ")
        check_item(item_to_check)
    elif choice == '5':
        clear_list()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
