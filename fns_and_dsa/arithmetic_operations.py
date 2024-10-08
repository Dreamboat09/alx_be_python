def perform_operation(num1, num2, operation):
    
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    operation = input('Enter the operation (add, subtract, multiply, divide): ').lower()
    result = 0
    
    if operation == 'add':
        result = num1 + num2
        
    elif operation == 'subtract':
        result = num1 - num2
    
    elif operation == 'multiply':
        result = num1 * num2
    
    elif operation == 'divide':
        if num2 == 0:
            print('error; division by zero is underfined')
        else:
            result = num1 / num2
    
    else:
        print('error')
        
        return perform_operation()