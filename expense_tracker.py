# File name where expenses will be saved
FILE_NAME = "expense.txt"

# Function to add a new expense
def add_expense():
    # Ask user for expense details
    name = input("Enter expenses name: ")
    amount = input("Enter amount: ")
    
    # Open file in append mode and save expense
    with open(FILE_NAME, "a") as file:
        file.write(name + "," + amount + "\n")
        print("Expense saved successfully!\n")
        
# Function to view all saved expenses
def view_expenses():
    try:
        # Open file in read mode
        with open(FILE_NAME,"r") as file:
            expenses = file.readlines()
            
            # If no expenses found
            if not expenses:
                print("No expenses recorded.\n")
                return
            
            # Display expenses one by one
            print("\n Your Expenses:")
            for i, expense in enumerate(expenses, start=1):
                name, amount = expense.strip().split(",")
                print(f"{i}. {name} - ₹ {amount}")
            print()
    except FileNotFoundError: 
        # If file does not exist
        print("No expenses found.\n")
        
# Function to calculate total expenses
def total_expense():
    total = 0
    try:
        # Read file line by line
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, amount = line.strip().split(",")
                total += float(amount)  # Add amount to total
        # Print total after loop
        print(f"\n Total expense: ₹ {total}\n")
    except FileNotFoundError:
        print("No expense found.\n")

# Menu function to interact with user
def menu():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expenses")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice!\n")

# Start the program
menu()