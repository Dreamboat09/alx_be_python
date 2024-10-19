def safe_divide(numerator, denominator):
    
    try:
        return float(numerator) / float(denominator)
        
    except ZeroDivisionError(Exception):
        print('Error: Cannot divide by zero.')
        
    except ValueError(Exception):
        print('Error: Please enter numeric values only')
        
    if __name__ == '__main__':
        safe_divide()