import re

def check_password_strength(password):
    # Initialize strength score and feedback list
    score = 0
    feedback = []

    # Rule 1: Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters).")

    # Rule 2: Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Rule 3: Uppercase and Lowercase
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Rule 4: Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., @, #, $).")

    # Determine Rating
    if score >= 5:
        rating = "Strong"
    elif score >= 3:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, feedback

# Main Execution
if __name__ == "__main__":
    print("--- Cybersecurity Tool: Password Strength Auditor ---")
    user_input = input("Enter a password to test: ")
    
    strength, suggestions = check_password_strength(user_input)
    
    print(f"\nStrength Rating: {strength}")
    if suggestions:
        print("Suggestions for improvement:")
        for note in suggestions:
            print(f" - {note}")
