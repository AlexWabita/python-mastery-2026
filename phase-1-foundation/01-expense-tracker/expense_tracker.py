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

def main():
    """Main Program loop"""
    print("Welcome to your personal Expense Tracker!")

    while True:     # Keeps the code running forever until a break is initiated
        show_menu()
        choice = input("\nEnter your choice (1-7): ")

        if choice == '1':
            print("Add expense - Coming soon!")
        elif choice == '2':
            print("View expense - Coming soon!")
        elif choice == '3':
            print("VTotal Spending - Coming soon!")
        elif choice == '4':
            print("Filter by Category - Coming soon!")
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