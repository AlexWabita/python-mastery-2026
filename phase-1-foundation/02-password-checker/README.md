# Password Strength Checker

A command-line tool that evaluates password strength based on security best practices and provides actionable feedback for improvement.

## Project Overview

This is my second project in my Python mastery journey. It builds on concepts from Project 1.1 while introducing new string manipulation techniques, validation logic, and security awareness.

## Features

### Core Functionality
- **Password Strength Analysis**: Evaluates passwords against 6 security criteria
- **Real-time Feedback**: Shows what's good and what's missing
- **Strength Rating**: Classifies passwords as Weak, Medium, Strong, or Very Strong
- **Common Password Detection**: Blocks commonly used passwords
- **Interactive Interface**: Check multiple passwords in one session
- **Security Tips**: Provides guidance on creating strong passwords

### Security Criteria Checked
1. **Minimum Length**: At least 8 characters (12+ recommended)
2. **Uppercase Letters**: Contains A-Z
3. **Lowercase Letters**: Contains a-z
4. **Numbers**: Contains 0-9
5. **Special Characters**: Contains !@#$%^&*()_+-=[]{}|;:,.<>?
6. **Not Common**: Rejects 24+ commonly used passwords

### Strength Ratings
- **Very Strong** (6-7 points): Meets all criteria + 12+ characters
- **Strong** (5 points): Meets all criteria, 8-11 characters
- **Medium** (3-4 points): Meets some criteria
- **Weak** (0-2 points): Fails multiple criteria or is a common password

## What I Learned

### New Python Concepts
- **String Methods**: `.isupper()`, `.islower()`, `.isdigit()`, `.lower()`
- **any() Function**: Check if at least one item in a sequence is True
- **Generator Expressions**: `(char.isupper() for char in password)`
- **Tuples**: Returning multiple values from functions
- **Conditional Logic**: Complex if/elif chains for scoring
- **String Membership**: `char in special_characters`

### Reinforced Concepts from Project 1.1
- Function design and organization
- While loops for program flow
- User input validation
- Docstrings for documentation
- The `if __name__ == "__main__":` pattern

### Key Insights
- **Character-level Operations**: How to check individual characters in strings
- **any() vs all()**: `any()` returns True if ONE item is True; stops early for efficiency
- **Normalization**: Using `.lower()` to handle case-insensitive comparisons
- **Security Thinking**: Why common passwords are dangerous even if they meet technical criteria
- **User Experience**: Providing helpful feedback, not just pass/fail

## How to Use

### Requirements
- Python 3.11.9 or higher
- No external dependencies (uses Python standard library only)

### Running the Application
```bash
# Navigate to the project directory
cd phase-1-foundation/02-password-checker

# Run the program
python password_checker.py
```

### Example Session
```
==================================================
       PASSWORD STRENGTH CHECKER
==================================================

This tool checks password strength based on:
  • Length (8+ characters, 12+ is better)
  • Uppercase and lowercase letters
  • Numbers
  • Special characters (!@#$%^&* etc.)
  • Not a common password

--------------------------------------------------

Enter a password to check (or 'quit' to exit): password

==================================================
PASSWORD STRENGTH: Weak (0/7 points)
==================================================

Details:
  ⛔ This is a commonly used password - NEVER use it!
  ❌ Too short (minimum 8 characters)
  ❌ Missing uppercase letters (A-Z)
  ❌ Missing numbers (0-9)
  ❌ Missing special characters (!@#$%^&* etc.)

==================================================

💡 TIP: Create a strong password by combining:
   - A memorable phrase
   - Mix of upper/lowercase
   - Numbers and special characters
   - At least 12 characters long

--------------------------------------------------

Enter a password to check (or 'quit' to exit): MyP@ssw0rd2026!

==================================================
PASSWORD STRENGTH: Very Strong (7/7 points)
==================================================

Details:
  ✅ Excellent length (12+ characters)
  ✅ Has uppercase letters
  ✅ Has lowercase letters
  ✅ Has numbers
  ✅ Has special characters

==================================================
```

## Project Structure
```
02-password-checker/
├── password_checker.py    # Main application code
├── README.md             # Project documentation (this file)
├── requirements.txt      # Dependencies (empty - uses stdlib)
└── .gitignore           # Git ignore rules
```

## Technical Implementation

### Function Breakdown

- `check_length(password, min_length)`: Validates minimum password length
- `has_uppercase(password)`: Checks for uppercase letters using `any()` and `.isupper()`
- `has_lowercase(password)`: Checks for lowercase letters using `any()` and `.islower()`
- `has_digit(password)`: Checks for digits using `any()` and `.isdigit()`
- `has_special_char(password)`: Checks for special characters using membership testing
- `is_common_password(password)`: Compares against list of 24 common passwords
- `check_password_strength(password)`: Main logic - calculates score and generates feedback
- `display_strength(score, strength, feedback)`: Formats and displays results
- `main()`: Program loop and user interface

## Challenges Faced & Solutions

1. **Understanding any() Function**: Initially confused about how `any()` works
   - **Solution**: Learned it returns True if at least ONE item is True, stops checking early

2. **Case Sensitivity in Common Passwords**: User could bypass check with "Password" vs "password"
   - **Solution**: Normalize to lowercase with `.lower()` before checking

3. **Providing Useful Feedback**: Just showing "weak" isn't helpful
   - **Solution**: Created detailed feedback list showing exactly what's missing

## Cybersecurity Concepts Applied

- **Defense in Depth**: Multiple criteria ensure stronger passwords
- **Known Bad Patterns**: Blocking common passwords prevents dictionary attacks
- **User Education**: Explaining WHY rules matter, not just enforcing them
- **Transparency**: Showing users exactly what makes a password strong

## Future Enhancements (Version 2.0 - Cybersecurity Focus)

- **HIBP Integration**: Check against Have I Been Pwned database for breached passwords
- **Entropy Calculation**: Measure true password randomness
- **Password Generation**: Create cryptographically secure random passwords
- **Zxcvbn Algorithm**: Implement more sophisticated strength analysis
- **Security Audit Log**: Track password checks with timestamps
- **Pattern Detection**: Identify keyboard patterns (qwerty), repeating chars, sequences (123)

## Completion Status

✅ **COMPLETED (v1.0)** - January 2026

This project demonstrates understanding of string manipulation, validation logic, function design, and basic security principles. Version 2.0 will incorporate advanced cybersecurity concepts and trends.

---

**Part of**: [Python Mastery 2026](https://github.com/AlexWabita/python-mastery-2026)  
**Phase**: 1 - Foundation Through Action  
**Developer**: [Alex Wabita](https://github.com/AlexWabita)  
**Also relates to**: Cybersecurity Portfolio (future integration)