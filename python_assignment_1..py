import re

def check_password_strength(password):
    # Check for the minimum length
    if len(password) < 8:
        return False

    # Check for uppercase and lowercase letters
    if not any(pwd.isupper() for pwd in password) or not any(pwd.islower() for pwd in password):
        return False

    # Check for at least one digit
    if not any(pwd.isdigit() for pwd in password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\]', password):
        return False

    return True

def main():
    password = input("Enter a password: ")

    if check_password_strength(password):
        print("Password is strong and meets the criteria.")
    else:
        print("Password is weak. Please make sure it meets the criteria.")

if __name__ == "__main__":
    main()
