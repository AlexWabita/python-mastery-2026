import re

def check_length(password, min_length=8):
    """
    Check if password meets minimum length requirement.
    
    Args:
        password: The password string to check
        min_length: Minimum required length (default 8)
    
    Returns:
        Boolean: True if password is long enough, False otherwise
    """
    return len(password) >= min_length


def has_uppercase(password):
    """Check if password contains at least one uppercase letter."""
    return any(char.isupper() for char in password)


def has_lowercase(password):
    """Check if password contains at least one lowercase letter."""
    return any(char.islower() for char in password)


def has_digit(password):
    """Check if password contains at least one digit."""
    return any(char.isdigit() for char in password)


def has_special_char(password):
    """Check if password contains at least one special character."""
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    return any(char in special_characters for char in password)



def is_common_password(password):
    """
    Check if password is in the list of commonly used passwords.
    
    Returns:
        Boolean: True if password is common (bad!), False if not common (good!)
    """
    common_passwords = [
        "password", "123456", "12345678", "qwerty", "abc123",
        "monkey", "1234567", "letmein", "trustno1", "dragon",
        "baseball", "iloveyou", "master", "sunshine", "ashley",
        "bailey", "passw0rd", "shadow", "123123", "654321",
        "superman", "qazwsx", "michael", "football", "1234", "0000", "0987", "09876543", "00000000"
    ]
    
    # Check if password (in lowercase) matches any common password
    return password.lower() in common_passwords


def check_password_strength(password):
    """
    Evaluate password strength based on multiple criteria.
    
    Returns:
        tuple: (strength_score, strength_label, feedback_list)
    """
    score = 0
    feedback = []
    
    # Check each criterion and give points
    if check_length(password, 8):
        score += 1
    else:
        feedback.append("❌ Too short (minimum 8 characters)")
    
    if check_length(password, 12):
        score += 1
        feedback.append("✅ Excellent length (12+ characters)")
    elif check_length(password, 8):
        feedback.append("⚠️  Good length, but 12+ is better")
    
    if has_uppercase(password):
        score += 1
        feedback.append("✅ Has uppercase letters")
    else:
        feedback.append("❌ Missing uppercase letters (A-Z)")
    
    if has_lowercase(password):
        score += 1
        feedback.append("✅ Has lowercase letters")
    else:
        feedback.append("❌ Missing lowercase letters (a-z)")
    
    if has_digit(password):
        score += 1
        feedback.append("✅ Has numbers")
    else:
        feedback.append("❌ Missing numbers (0-9)")
    
    if has_special_char(password):
        score += 1
        feedback.append("✅ Has special characters")
    else:
        feedback.append("❌ Missing special characters (!@#$%^&* etc.)")
    
    # Check for common passwords
    if is_common_password(password):
        score = 0  # Override score to 0 if it's a common password
        feedback.insert(0, "⛔ This is a commonly used password - NEVER use it!")
    
    # Determine strength label based on score
    if score >= 6:
        strength = "Very Strong"
    elif score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return score, strength, feedback



def display_strength(score, strength, feedback):
    """Display password strength results in a formatted way."""
    print("\n" + "="*50)
    print(f"PASSWORD STRENGTH: {strength} ({score}/7 points)")
    print("="*50)
    
    print("\nDetails:")
    for item in feedback:
        print(f"  {item}")
    
    print("\n" + "="*50)


def main():
    """Main program loop."""
    print("="*50)
    print("       PASSWORD STRENGTH CHECKER")
    print("="*50)
    print("\nThis tool checks password strength based on:")
    print("  • Length (8+ characters, 12+ is better)")
    print("  • Uppercase and lowercase letters")
    print("  • Numbers")
    print("  • Special characters (!@#$%^&* etc.)")
    print("  • Not a common password")
    
    while True:
        print("\n" + "-"*50)
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("\nThanks for using Password Strength Checker!")
            break
        
        if len(password) == 0:
            print("⚠️  Password cannot be empty!")
            continue
        
        score, strength, feedback = check_password_strength(password)
        display_strength(score, strength, feedback)
        
        # Give improvement suggestions
        if strength in ["Weak", "Medium"]:
            print("\n💡 TIP: Create a strong password by combining:")
            print("   - A memorable phrase")
            print("   - Mix of upper/lowercase")
            print("   - Numbers and special characters")
            print("   - At least 12 characters long")


# Run the program
if __name__ == "__main__":
    main()