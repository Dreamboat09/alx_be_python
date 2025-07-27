num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case "+":
        result = (num1 + num2)
    case "-":
        result = (num1 - num2)
    case "*":
        result = (num1 * num2)
    case "/":
        result = (num1 / num2)

print(f"The result is {result}.")
