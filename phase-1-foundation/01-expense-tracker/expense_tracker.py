"""
Personal Expense Tracker
A simple CLI tool to manage daily expensis
"""

# This list will store all of our expenses
expenses = []   # This will be used to hold all our expense dictionaries

def show_menu():    # 'def' used to define a function in our case to show menu
    """Display the main menu options"""
    print("\n" + "="*40)
    print("     PERSONAL EXPENSE TRACKER")
    print("="*40)
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Spending")
    print("4. View Expenses by Category")
    print("5. Save Expense")
    print("6. Load Expense")
    print("7. Exit")
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
        from datetime import date
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
    for cat in sorted(categories):
        print(f"  -  {cat}")
    print("="*40)

    # Ask user which category to filter
    filter_cat = input("\nEnter the category to view: ").lower()

    # filter expenses by caetegory
    filtered = []
    for expense in expenses:
        if expense['category'] == filter_cat:
            filtered.append(expense)
    
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


def main():
    """Main Program loop"""
    print("Welcome to your personal Expense Tracker!")

    while True:     # Keeps the code running forever until a break is initiated
        show_menu()
        choice = input("\nEnter your choice (1-7): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            calculate_total()
        elif choice == '4':
            view_by_category()
        elif choice == '5':
            print("save - Coming soon!")
        elif choice == '6':
            print("Load - Coming soon!")
        elif choice == '7':
            print("\nThank you for using Expense Tracker. Goodbye!")
            break   # exits the loop
        else:
            print("\n❌ Invalid choioce! Please enter a number between 1-7.")


# This runs the program
if __name__ == "__main__":  # Means run main() when the file is executed directly
    main()