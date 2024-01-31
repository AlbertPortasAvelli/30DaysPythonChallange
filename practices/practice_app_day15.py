def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError("Cannot divide by zero.")

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def get_operation_input():
    valid_operations = ['+', '-', '*', '/']
    while True:
        operation = input("Enter the operation (+, -, *, /): ")
        if operation in valid_operations:
            return operation
        else:
            print("Error: Invalid operation entered.")

def calculator():
    while True:
        try:
            num1 = get_number_input("Enter the first number: ")
            operation = get_operation_input()
            num2 = get_number_input("Enter the second number: ")

            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)

            print(f"Result: {result}")

        except (ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")

        try:
            continue_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if continue_calculation != 'yes':
                break
        except KeyboardInterrupt:
            print("Exiting calculator.")
            break

if __name__ == "__main__":
    calculator()
