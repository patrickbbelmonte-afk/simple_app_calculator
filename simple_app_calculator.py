def calculate(first_number, second_number, operation):
    """Perform the selected math operation."""
    if operation == 1:
        return first_number + second_number
    elif operation == 2:
        return first_number - second_number
    elif operation == 3:
        return first_number * second_number
    elif operation == 4:
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number

while True:
    print("\n=== SIMPLE CALCULATOR ===")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")

    try:
        user_choice = int(input("Choose operation (1-4): "))

        if user_choice not in [1, 2, 3, 4]:
            print("Invalid choice. Try again.")
            continue

        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        result = calculate(first_number, second_number, user_choice)
        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except ZeroDivisionError as error:
        print("Error:", error)

    if input("Try again? (yes/no): ").lower() != "yes":
        print("Thank you!")
        break