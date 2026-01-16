import json     # We'll use JSON format (JavaScript Object Notation) - a standard way to store data.
from datetime import date
import os

"""
Personal Expense Tracker
A simple CLI tool to manage daily expensis
"""


# This list will store all of our expenses
expenses = []   # This will be used to hold all our expense dictionaries


# Function to clear screen in the terminal
def clear_screen():
    """Clear the terminal Screen"""
    # Check the OS of the system
    if os.name == 'nt':
        os.system('cls')
    else:       # Mac/Linux
        os.system('clear')
    
    print("✨ Screen cleared!\n")


def show_menu():    # 'def' used to define a function in our case to show menu
    """Display the main menu options"""
    print("\n" + "="*40)
    print("     PERSONAL EXPENSE TRACKER")
    print("="*40)
    print("1.   Add Expense")
    print("2.   View All Expense")
    print("3.   View Total Spending")
    print("4.   View Expenses by Category")
    print("5.   Delete Expense")
    print("6.   Delete Expenses by Category")
    print("7.   Save Expense")
    print("8.   Load Expense")
    print("9.   clear Screen")
    print("10.  Exit")
    print("="*40)


def add_expense():
    """Add new expense to the tracker"""
    print("\n" + "="*40)
    print("     ADD NEW EXPENSE")
    print("="*40)

    # Get expense details from user

    try:        # Try to do this code
        # Get amount and convert to float
        amount = float(input("Enter amount (e.g., 42.50): "))

        # Get category
        category = input("Enter category (e.g., food, transport, entertainment): ").lower()     # Helps with consistency by keeping everything in lower case

        # Get description
        description = input("Enter description: ")

        # Get date
        today = date.today().strftime("%Y-%m-%d")   # Gets today's date

        # Create expense dictionary
        expense = {
            'amount': amount,   # Key: value
            'category': category,
            'description': description,
            'date': today
        }

        # Add to expense list
        expenses.append(expense)    # .append() adds item to the end a list

        print(f"\n✅ Expense added successfully!")
        print(f"    Amount: ${amount:.2f}")     # {amount:.2f} formats the number to 2 decimal places
        print(f"    Category: {category}")
        print(f"    Description: {description}")
        print(f"    Date: {today}")

    except ValueError:      # If there's a ValueError (user types "abc" instead of a number)     # Do this instead
        print("\n❌ Error: Please enter a valid number for amount!")


def view_expenses():
    """Display all expenses"""
    if not expenses:    # if list is empty
        print("\n📭 No expenses recorded yet!")
        return  # Exits the function early
    
    print("\n" + "="*60)
    print("                     ALL EXPENSES")
    print("="*60)

    # Loop through each expense in the list
    for i, expense in enumerate(expenses, 1):    # enumerate gives us: i = the index/position (starting at 1) and expense = the actuall expense dictionary
        print(f"\n#{i}")
        print(f"    Date:           {expense['date']}")
        print(f"    Category:       {expense['category']}")
        print(f"    Description:    {expense['description']}")
        print(f"    Amount:         {expense['amount']}")
        print("-"*60)


def calculate_total():
    """Calculate and show total spendind"""
    if not expenses:
        print("\n📭  No expenses to calculate!")
        return

    # Calculate total by adding up all amount
    total = 0
    for expense in expenses:
        total += expense['amount']

    print("\n" + "="*40)
    print("         SPENDING SUMMARY")
    print("="*40)
    print(f"Total Expenses: {len(expenses)}")
    print(f"Total Amount:   ${total:.2f}")
    print(f"Average:        ${total / len(expenses):.2f}")
    print("="*40)


def view_by_category():
    """View expenses filtered by category"""
    if not expenses:
        print("\n📭 No expenses recorded yet!")
        return

    # Get all unique categories
    categories = set()  # 'set' stalls uique values only
    for expense in expenses:
        categories.add(expense['category'])

    # Show available categories
    print("\n" + "="*40)
    print("Available categories:")
    for cat in sorted(categories):  # Sorts the available categories
        print(f"  -  {cat}")
    print("="*40)

    # Ask user which category to filter
    filter_cat = input("\nEnter the category to view: ").lower()

    # filter expenses by caetegory
    filtered = []   # Empty list
    for expense in expenses:
        if expense['category'] == filter_cat:   # Check condition
            filtered.append(expense)            # Add if the condition matches
    
    # Display thr filtered results
    if not filtered:
        print(f"\n❌ No expenses found in category '{filter_cat}'")
        return
    
    print(f"\n{'='*60}")
    print(f"    EXPENSES IN CATEGORY: {filter_cat}")
    print("="*60)

    category_total = 0
    for i, expense in enumerate(filtered, 1):
        print(f"\n#{i}")
        print(f"  Date:        {expense['date']}")
        print(f"  Description: {expense['description']}")
        print(f"  Amount:      ${expense['amount']:.2f}")
        category_total += expense['amount']
        print("-" * 60)

    print(f"\nTotal for {filter_cat}: ${category_total:.2f}")


def delete_expense():
    """Delete an expense from the tracker"""
    if not expenses:
        print("\n📭 No expenses to delete")
        return
    
    # Show all expenses with numbers
    print("\n" + "="*60)
    print("                 DELETE EXPENSES")
    print("="*60)

    for i, expense in enumerate(expenses, 1):
        print(f"\n#{i}")
        print(f"  Date:        {expense['date']}")
        print(f"  Category:    {expense['category']}")
        print(f"  Description: {expense['description']}")
        print(f"  Amount:      ${expense['amount']:.2f}")
        print("-" * 60)

    # Ask which one to delete
    try:
        choice = input("\nEnter expense number to delete (or 0 to cancel): ")
        choice = int(choice)

        if choice == 0:
            print("\n❌ Delete Cancelled.")
            return
        
        if 1 <= choice <= len(expenses):
            # Get the expense before deleting (to show confirmation)
            deleted = expenses[choice - 1] # we've used -1 because list starts at 0

            # Delete it from the list
            expenses.pop(choice - 1)

            print(f"\n✅ Deleted expense:")
            print(f"    Category: {deleted['category']}")
            print(f"    Description: {deleted['description']}")
            print(f"    Amount: {deleted['amount']:.2f}")
        else:
            print(f"\n❌ Invalid number! Please enter 1-{len(expenses)}")
    
    except ValueError:
        print("\n❌ Please enter a valid number!")


def delete_by_category():
    """Delete all expenses in a specific category"""
    if not expenses:
        print("\n📭 No expenses to delete!")
        return
    
    # Get all unique categories
    categories = set()
    for expense in expenses:
        categories.add(expense['category'])
    
    # Show available categories
    print("\n" + "="*40)
    print("DELETE BY CATEGORY")
    print("="*40)
    print("Available categories:")
    for category in sorted(categories):
        count = sum(1 for exp in expenses if exp['category'] == category)
        print(f"  - {category} ({count} expenses)")
    print("="*40)
    
    # Ask which category
    category = input("\nEnter category to delete (or press Enter to cancel): ").lower()
    
    if not category:
        print("\n❌ Delete cancelled.")
        return
    
    # Find all expenses in this category
    to_delete = [exp for exp in expenses if exp['category'] == category]
    
    if not to_delete:
        print(f"\n❌ No expenses found in category '{category}'")
        return
    
    # Ask for confirmation
    print(f"\n⚠️  WARNING: This will delete {len(to_delete)} expense(s)!")
    confirm = input("Type 'yes' to confirm: ").lower()
    
    if confirm == 'yes':
        # Delete using a loop instead of reassignment
        # This modifies the list in place, no global needed!
        for exp in to_delete:
            expenses.remove(exp)
        print(f"\n✅ Deleted {len(to_delete)} expense(s) from '{category}'")
    else:
        print("\n❌ Delete cancelled.")


def save_expenses():
    """Save expenses to a JSON file"""
    if not expenses:
        print("\n📭 No expenses to save!")
        return
    
    try:
        # Open file in write mode
        with open('data/expenses.json', 'w') as file:
            json.dump(expenses, file, indent=4)      # saves with nice formating
            # file automaticaly closes when done
        print(f"\n✅ Successfully saved {len(expenses)} expenses to file!")
    
    except Exception as e:
        print(f"\n❌ Error saving file: {e}")



def load_expenses():
    """Load expenses from JSON file"""
    global expenses     # we need to modify the gloabal expenses list which is 'global'

    try:
        # Open file in read mode
        with open('data/expenses.json', 'r') as file:
            expenses = json.load(file)      # loads data from file
        
        print(f"\n✅ Successfully loaded {len('expenses')} expenses from file!")
    
    except FileNotFoundError:       # Handles this specific error
        print("\n📭 No saved expenses found. Starting fresh!")
    
    except Exception as e:      # Catches any other error
        print(f"\n❌ Error loading file: {e}")


def main():
    """Main Program loop"""
    print("Welcome to your personal Expense Tracker!")

    while True:     # Keeps the code running forever until a break is initiated
        show_menu()
        choice = input("\nEnter your choice (1-10): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            calculate_total()
        elif choice == '4':
            view_by_category()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            delete_by_category()
        elif choice == '7':
            save_expenses()
        elif choice == '8':
            load_expenses()
        elif choice == '9':
            clear_screen()
        elif choice == '10':
            print("\nThank you for using Expense Tracker. Goodbye!")
            break   # exits the loop
        else:
            print("\n❌ Invalid choioce! Please enter a number between 1-10.")


# This runs the program
if __name__ == "__main__":  # Means run main() when the file is executed directly
    main()