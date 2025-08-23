#    define a function
def safe_divide(numerator: float, denominator: float):

    try:
        result = float(numerator)/ float(denominator)
    except ZeroDivisionError:
        "Error: Cannot divide by zero."
    except ValueError:
        "Error: Please enter numeric values only."
    else: 
        f"The result of the division is {result}"