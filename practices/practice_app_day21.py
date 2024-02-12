class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        self.expenses.append({'amount': amount, 'category': category, 'description': description})
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
        else:
            print("Expenses:")
            for idx, expense in enumerate(self.expenses, start=1):
                print(f"{idx}. Amount: ${expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

    def update_expense(self, expense_index, amount, category, description):
        if 0 < expense_index <= len(self.expenses):
            self.expenses[expense_index - 1] = {'amount': amount, 'category': category, 'description': description}
            print("Expense updated successfully!")
        else:
            print("Invalid expense index.")

    def delete_expense(self, expense_index):
        if 0 < expense_index <= len(self.expenses):
            del self.expenses[expense_index - 1]
            print("Expense deleted successfully!")
        else:
            print("Invalid expense index.")


def main():
    print("Welcome to Expense Tracker App!")

    expense_tracker = ExpenseTracker()

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter expense description: ")
            expense_tracker.add_expense(amount, category, description)

        elif choice == "2":
            expense_tracker.view_expenses()

        elif choice == "3":
            expense_index = int(input("Enter expense index to update: "))
            amount = float(input("Enter new expense amount: "))
            category = input("Enter new expense category: ")
            description = input("Enter new expense description: ")
            expense_tracker.update_expense(expense_index, amount, category, description)

        elif choice == "4":
            expense_index = int(input("Enter expense index to delete: "))
            expense_tracker.delete_expense(expense_index)

        elif choice == "5":
            print("Thank you for using Expense Tracker App!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()