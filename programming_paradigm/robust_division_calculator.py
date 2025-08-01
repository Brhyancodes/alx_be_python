def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Try the division
        result = numerator / denominator

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    else:
        return f"The result of the division is {result}"
