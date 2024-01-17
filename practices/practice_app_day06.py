# Employee Management System

def add_employee(employees, employee_id, name, position, salary):
    new_employee = (employee_id, name, position, salary)
    employees.append(new_employee)
    print("Employee added successfully!")

def display_employees(employees):
    print("\nList of Employees:")
    for employee in employees:
        print(f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}, Salary: ${employee[3]}")

def search_employee(employees, employee_id):
    for employee in employees:
        if employee[0] == employee_id:
            print("\nEmployee Found:")
            print(f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}, Salary: ${employee[3]}")
            return
    print("\nEmployee not found!")

def calculate_total_salary(employees):
    total_salary = sum(employee[3] for employee in employees)
    print(f"\nTotal Salary of all employees: ${total_salary}")

def main():
    employees = []

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Calculate Total Salary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            position = input("Enter Employee Position: ")
            salary = float(input("Enter Employee Salary: "))
            add_employee(employees, employee_id, name, position, salary)

        elif choice == '2':
            display_employees(employees)

        elif choice == '3':
            employee_id = input("Enter Employee ID to search: ")
            search_employee(employees, employee_id)

        elif choice == '4':
            calculate_total_salary(employees)

        elif choice == '5':
            print("Exiting Employee Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
