def safe_divide(numerator, denominator):
    
    try:
        ans = float(numerator) / float(denominator) 
        return f'The result of the division is {ans}'
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
        
    except ValueError:
       return "Error: Please enter numeric values only."
