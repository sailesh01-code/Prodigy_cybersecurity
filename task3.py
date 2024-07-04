import re

def assess_password_strength(password):
    length = len(password)
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_number = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*()-+=_]', password))

    strength = 0

    # Assess based on length
    if length >= 8:
        strength += 1
    if length >= 12:
        strength += 1

    # Assess based on character types
    if has_uppercase and has_lowercase:
        strength += 1
    if has_number:
        strength += 1
    if has_special:
        strength += 1

    return strength

def main():
    password = input("Enter your password: ")
    strength = assess_password_strength(password)

    if strength == 0:
        print("Weak password! It's too short.")
    elif strength == 1:
        print("Moderate password. Consider adding more complexity.")
    elif strength == 2:
        print("Fairly strong password. Good job!")
    elif strength == 3:
        print("Strong password! Keep it up.")
    elif strength == 4:
        print("Very strong password! You're doing great!")

if __name__ == "__main__":
    main()