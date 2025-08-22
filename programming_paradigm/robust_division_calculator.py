#    define a function
def safe_divide(numerator: float, denominator: float):

    try:
        result = float(numerator)/ float(denominator)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    else: 
        print(f"The result of the division is {result}")
