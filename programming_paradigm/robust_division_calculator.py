def safe_divide(numerator, denominator):
    
    try:
        ans = float(numerator) / float(denominator) 
        return f'The result of the division is {ans}'
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        
    except ValueError:
       print("Error: Please enter numeric values only.")
    
    if __name__ == '__main__':
        safe_divide()