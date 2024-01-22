# Simple Employee Management App
# Employee database
employees = {
    '001': {'name': 'Alice', 'position': 'Developer', 'status': 'Active'},
    '002': {'name': 'Bob', 'position': 'Designer', 'status': 'Inactive'},
    '003': {'name': 'Charlie', 'position': 'Manager', 'status': 'Active'},
}

def show_employee_info(employee_id):
    if employee_id in employees:
        employee = employees[employee_id]
        print(f"Employee ID: {employee_id}")
        print(f"Name: {employee['name']}")
        print(f"Position: {employee['position']}")
        print(f"Status: {employee['status']}")
    else:
        print("Employee not found.")

def update_employee_status(employee_id, new_status):
    if employee_id in employees:
        employees[employee_id]['status'] = new_status
        print(f"Employee {employee_id}'s status updated to {new_status}.")
    else:
        print("Employee not found.")

# Main program
while True:
    print("\nEmployee Management App")
    print("1. Show Employee Information")
    print("2. Update Employee Status")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, 3): ")

    if choice == '1':
        employee_id = input("Enter employee ID: ")
        show_employee_info(employee_id)

    elif choice == '2':
        employee_id = input("Enter employee ID: ")
        new_status = input("Enter new status (Active/Inactive): ")
        if new_status.lower() in ['active', 'inactive']:
            update_employee_status(employee_id, new_status.capitalize())
        else:
            print("Invalid status. Please enter 'Active' or 'Inactive'.")

    elif choice == '3':
        print("Exiting the Employee Management App. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
