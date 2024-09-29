num1 = int(input('Enter the first number: '))
 
num2 = int(input('Enter the second number: '))
 
operation = input('Choose the operation (+, -, *, /): ')
 
match operation:
    case _ if operation == '+':
        result = num1 + num2
        print(f'The result is {result}.')
    case _ if operation == '-':
        result = num1 - num2
        print(f'The result is {result}.')
    case _ if operation == '*':
       result = num1 * num2
       print(f'The result is {result}.')
    case _ if operation == '/':
        result = num1 // num2
        if operation == '0':
            print('error, indivisible by 0')
        else:
            print(f'The result is {result}.')
    case _:
        print('error') 