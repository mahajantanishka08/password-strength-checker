def check_password_strength(password):
    length = len(password) >= 8
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in "!@#$%^&*()-_=+[]{};:,.<>?/" for c in password)

    score = sum([length, upper, lower, digit, special])

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"

if __name__ == "__main__":
    pwd = input("Enter password: ")
    print("Strength:", check_password_strength(pwd))
