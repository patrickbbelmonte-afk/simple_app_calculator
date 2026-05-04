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
