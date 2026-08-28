# age_check.py
"""
A simple script that asks the user for their age and prints a message
based on the entered value. It also handles non‑numeric input gracefully.
"""

def main():
    """Prompt the user for their age and respond accordingly."""
    try:
        # Ask the user for input. The input() function always returns a string.
        age_input = input("Please enter your age: ")
        # Convert the string to an integer. This will raise ValueError if the
        # input is not a valid integer representation.
        age = int(age_input)
    except ValueError:
        # The user entered something that cannot be converted to an int.
        print("Invalid input. Please enter a numeric value for age.")
        return

    # Basic validation – age should be a non‑negative number.
    if age < 0:
        print("Age cannot be negative. Please try again.")
        return

    # Determine which message to display based on the age.
    if age < 18:
        print("You are a minor.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are a senior.")


if __name__ == "__main__":
    main()
