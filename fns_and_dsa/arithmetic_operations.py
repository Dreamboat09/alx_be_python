# define the function and assign parameters to it

def perform_operation (num1, num2, operation):
    # perform the operations
    if operation == "add":
        return num1 + num2
    
    elif operation == "subtract":
        return num1 - num1
    
    elif operation == "multiply":
        return num1 * num2
    
    elif operation == "divide":
        # handling division by zero
        if num2 == 0:
            return "indivisible by zero(0)"
        else:
            return num1 / num2
    
    else:
        return 'wrong operation'