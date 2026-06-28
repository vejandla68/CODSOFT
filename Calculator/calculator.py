# -----------------------------------------
# Project: Simple Calculator
# Author: Vejandla Mukthesh Kumar
# -----------------------------------------

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    return num1 / num2


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def display_menu():
    print("\n" + "=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main():

    print("Welcome to the Python Calculator!")

    while True:

        display_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("\nThank you for using the calculator.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please try again.")
            continue

        first_number = get_number("Enter first number : ")
        second_number = get_number("Enter second number: ")

        if choice == "1":
            result = add(first_number, second_number)
            operator = "+"

        elif choice == "2":
            result = subtract(first_number, second_number)
            operator = "-"

        elif choice == "3":
            result = multiply(first_number, second_number)
            operator = "*"

        else:
            result = divide(first_number, second_number)
            operator = "/"

        print("\n------------------------------")
        print(f"{first_number} {operator} {second_number} = {result}")
        print("------------------------------")

        repeat = input("\nDo you want another calculation? (yes/no): ").strip().lower()

        if repeat != "yes":
            print("\nProgram Closed.")
            break


if __name__ == "__main__":
    main()
