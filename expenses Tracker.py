
import os
import datetime

#File where expenses will be stored
expense_file = "espenses.txt"
#Function to Add Expense
def addExpense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        date = input("Enter date (YYYY/MM/DD): ")

        if date.strip == " ":
            date = str(datetime.date.today())

        with open(expense_file, "a") as file:
            file.write(f"{date}, {amount}, {category}, {description}\n")

        print("EXPENSE SAVED SUCCESSFULLY!\n")

    except ValueError:
        print("Error: invalid amount. Please enter a number.\n ")
#Function to View Expense
def viewExpenses():
    if not os.path.exists(expense_file):
        print("No expenses recorded yet.\n")
        return
    
    print("\n***** ALL EXPENSES *****")
    with open(expense_file, "r") as file:
        for line in file:
            date, amount, category, description = line.strip().split(",")
            print(f"{date} | ₱{amount} | {category} | {description}")
    print()
#Function to View Summary report
def viewSummary():
    if not os.path.exists(expense_file):
        print("No expense recoorded yet.\n")
        return
    
    total = 0
    categories = {}

    with open(expense_file, "r") as file:
        for line in file:
            date, amount, category, description = line.strip().split(",")
            amount = float(amount)
            total += amount
            categories[category] = categories.get(category, 0) + amount

    print("\n***** SUMMARY REPORT *****")
    print(f"Total Expenses: ₱{total:.2f}")
    for cat, amt in categories.items():
        print(f"{cat}: ₱{amt:.2f}")
    print()
#Function to Search Expenses by category or date
def searchExpenses():
    if not os.path.exists(expense_file):
        print("No expenses recorded yet.\n")
        return

    keyword = input("Enter category or date (YYYY-MM-DD) to search: ").lower()

    print("\n***** SEARCH REPORT *****")
    found = False
    with open(expense_file, "r") as file:
        for line in file:
            date, amount, category, description = line.strip().split(",")
            if keyword in category.lower() or keyword in date:
                print(f"{date} | ₱{amount} | {category} | {description}")
                found = True
    if not found:
        print("No matching expenses found.")
    print()
#Main program loop
def main():
     while True:
        print("***** EXPENSE TRACKER *****")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary Report")
        print("4. Search Expenses")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            addExpense()
        elif choice == "2":
            viewExpenses()
        elif choice == "3":
            viewSummary()
        elif choice == "4":
            searchExpenses()
        elif choice == "5":
            print("Exit. thank u!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()







    


