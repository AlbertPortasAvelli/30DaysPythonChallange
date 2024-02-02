def add_user(users, name, age):
    try:
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer.")
        
        users.append({'name': name, 'age': age})
        print(f"User '{name}' added successfully.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def display_users(users):
    try:
        if not users:
            raise ValueError("No users to display.")

        print("List of Users:")
        for index, user in enumerate(users, start=1):
            print(f"{index}. {user['name']} - {user['age']} years old")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    users = []

    # Adding users
    add_user(users, "Alice", 25)
    add_user(users, "Bob", 30)
    add_user(users, "Charlie", "InvalidAge")  # This will trigger an error

    # Displaying users
    display_users(users)

if __name__ == "__main__":
    main()
