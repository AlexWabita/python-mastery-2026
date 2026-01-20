# Personal Expense Tracker

A command-line application for tracking personal expenses with categorization, filtering, and data persistence.

## Project Overview

This is my first project in my Python mastery journey. It teaches fundamental Python concepts through a practical, real-world application that I can actually use to track my spending.

## Features

### Core Functionality
- **Add Expenses**: Record expenses with amount, category, and description
- **View All Expenses**: Display all recorded expenses in a formatted table
- **Calculate Statistics**: View total spending and average expense amount
- **Filter by Category**: View expenses from a specific category
- **Delete Expenses**: Remove individual expenses or clear entire categories
- **Data Persistence**: Automatically save and load expenses from JSON file

### Technical Features
- Cross-platform screen clearing (works on Windows and Linux)
- Automatic date stamping for each expense
- Input validation and error handling
- User-friendly menu interface
- Category management with predefined options

## What I Learned

### Python Concepts Mastered
- **Data Types**: strings, floats, integers, booleans
- **Data Structures**: lists, dictionaries, sets
- **Control Flow**: if/elif/else statements, while loops, for loops
- **Functions**: defining functions, parameters, return values, docstrings
- **File I/O**: reading and writing files using `with` statement
- **JSON**: serialization and deserialization with `json.dump()` and `json.load()`
- **Modules**: `datetime`, `json`, `os`
- **Error Handling**: try/except blocks for ValueError and FileNotFoundError
- **Global Variables**: when to use `global` keyword (reassignment vs modification)
- **List Comprehension**: filtering lists with `[item for item in list if condition]`
- **Built-in Functions**: `enumerate()`, `sorted()`, `len()`, `sum()`

### Key Insights
- **List Modification vs Reassignment**: Learned that `.append()`, `.remove()`, `.pop()` modify the list in place (no `global` needed), while `list = [...]` reassigns the variable (requires `global`)
- **Error Handling**: Why it's important to validate user input and handle file operations safely
- **Data Persistence**: How to save application state between sessions using JSON
- **Cross-platform Development**: Using `os.name` to write code that works on different operating systems

## How to Use

### Requirements
- Python 3.11.9 or higher
- No external dependencies (uses Python standard library only)

### Running the Application
```bash
# Navigate to the project directory
cd phase-1-foundation/01-expense-tracker

# Run the program
python expense_tracker.py
```

### Menu Options

1. **Add Expense**: Enter amount, select category, add description
2. **View All Expenses**: See all recorded expenses with date, category, amount, and description
3. **View Total & Average**: Calculate spending statistics
4. **View by Category**: Filter expenses by specific category
5. **Delete Expense**: Remove a single expense by number
6. **Delete Category**: Remove all expenses in a category
7. **Exit**: Save and close the application

### Available Categories
- Food
- Transport
- Entertainment
- Bills
- Shopping
- Health
- Other

## Project Structure
```
01-expense-tracker/
├── expense_tracker.py    # Main application code
├── README.md            # Project documentation (this file)
├── requirements.txt     # Dependencies (empty - uses stdlib)
├── .gitignore          # Git ignore rules
└── data/               # Data storage directory
    └── expenses.json   # Expense data file (created automatically)
```

## Sample Usage
```
=== Personal Expense Tracker ===

1. Add Expense
2. View All Expenses
3. View Total & Average
4. View by Category
5. Delete Expense
6. Delete Category
7. Exit

Choose an option (1-7): 1

Enter amount: 500
Select category:
1. Food
2. Transport
3. Entertainment
4. Bills
5. Shopping
6. Health
7. Other
Choose category (1-7): 1
Enter description: Lunch at Java House

Expense added successfully!
```

## Challenges Faced & Solutions

1. **Global Variable Confusion**: Initially confused about when to use `global` keyword
   - **Solution**: Learned that `global` is needed for reassignment, not for modifying list contents

2. **File Not Found on First Run**: Program crashed when expenses.json didn't exist
   - **Solution**: Added `FileNotFoundError` exception handling in `load_expenses()`

3. **Category Deletion Issues**: First attempt had bugs when deleting by category
   - **Solution**: Used list comprehension to create a new filtered list

## Future Enhancements (Ideas for Later)

- Add budget limits per category with warnings
- Generate monthly/weekly spending reports
- Export data to CSV for spreadsheet analysis
- Add expense editing functionality
- Implement date range filtering
- Add visual charts/graphs using libraries

## Completion Status

✅ **COMPLETED** - January 2026

This project successfully demonstrates understanding of Python fundamentals including data structures, file I/O, error handling, and user interface design.

---

**Part of**: [Python Mastery 2026](https://github.com/AlexWabita/python-mastery-2026)  
**Phase**: 1 - Foundation Through Action  
**Developer**: [Alex Wabita](https://github.com/AlexWabita)