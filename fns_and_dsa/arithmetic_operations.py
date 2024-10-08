def perform_operation ():
    
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    operation = input('Enter the operation (add, subtract, multiply, divide): ').lower()
    
    if operation == 'add':
        result = num1 + num2
        
    elif operation == 'subtract':
        result = num1 - num2
    
    elif operation == 'multiply':
        result = num1 * num2
    
    elif operation == 'divide':
        result = num1 / num2
    
    else:
        print('error')
        
        return perform_operation()