# Implement a division calculator that robustly handles errors like division by zero and non-numeric inputsi
# Create two Python scripts: robust_division_calculator.py, which contains the division logic including error handling
#+ and main.py, which interfaces with the user through the command line.

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator/denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    else:
        return f'The result of the division is {result}'

