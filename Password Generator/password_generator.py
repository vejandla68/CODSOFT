
# -----------------------------------------
# Project : Password Generator
# Internship : CodSoft Python Programming
# Name : Vejandla Mukthesh Kumar
# -----------------------------------------

import random
import string


def create_password(length, uppercase, lowercase, digits, symbols):

    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if digits:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if characters == "":
        return None

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("=" * 45)
print("        PASSWORD GENERATOR")
print("=" * 45)

while True:

    try:
        length = int(input("\nEnter password length: "))

        if length <= 0:
            print("Password length must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    print("\nChoose password complexity")

    upper = input("Include Uppercase Letters? (Y/N): ").strip().lower() == "y"
    lower = input("Include Lowercase Letters? (Y/N): ").strip().lower() == "y"
    numbers = input("Include Numbers? (Y/N): ").strip().lower() == "y"
    special = input("Include Special Characters? (Y/N): ").strip().lower() == "y"

    password = create_password(length, upper, lower, numbers, special)

    if password is None:
        print("\nPlease select at least one character type.")
    else:
        print("\nGenerated Password:")
        print(password)

    again = input("\nGenerate another password? (Y/N): ").strip().lower()

    if again != "y":
        print("\nThank you for using the Password Generator.")
        break
