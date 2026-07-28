# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def power(a, b):
    return a ** b

while True:
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")
    choice = input("Select an operation (1-7): ")

    if choice == "7":
        print("Goodbye!")
        break
    elif choice in ("1", "2", "3", "4", "5", "6"):
        a = float(input("Enter first number : "))
        b = float(input("Enter second number: "))
        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            result = divide(a, b)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print("Result:", result)
        elif choice == "5":
            result = modulus(a, b)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print("Result:", result)
        elif choice == "6":
            print("Result:", power(a, b))
    else:
        print("Invalid choice. Please try again.")