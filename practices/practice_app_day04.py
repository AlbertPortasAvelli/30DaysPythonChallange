import textwrap


def cross_effect(text):
    # Add cross effect to text
    return "̷".join(text.replace(" ", "̷"))

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

def add_task(tasks, title, description):
    task = Task(title, description)
    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks(tasks):
    print("Task List:")
    for i, task in enumerate(tasks, start=1):
        status = "[X]" if task.completed else "[ ]"

        print(f"{i}. {status} {task.title} - {task.description}")
    print()

def mark_as_completed(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        task = tasks[task_number - 1]
        task.completed = True
        print("Task marked as completed!\n")
    else:
        print("Invalid task number. Please try again.\n")

def save_and_exit(tasks):
    print("Tasks saved to file. Exiting...\n")
    # Add code to save tasks to a file (e.g., JSON, text file, etc.)
    exit()

def get_user_input():
    tasks = []
    while True:
        print("Welcome to Chic Strikethrough Task Tracker!")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark as Completed")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(tasks, title, description)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_as_completed(tasks, task_number)
        elif choice == "4":
            save_and_exit(tasks)
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    get_user_input()
