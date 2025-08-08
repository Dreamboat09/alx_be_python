FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR  = 9/5


def convert_to_celsius(fahrenheit):
    if type(temp) != float:
        print("Invalid temperature. Please enter a numeric value.")
    else:
        return (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    if type(temp) != float:
        print("Invalid temperature. Please enter a numeric value.")
    else:
        return (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


temp = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if unit == "C":
    new_temp = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {new_temp}°F")

elif unit == "F":
    new_temp = convert_to_celsius(temp)
    print(f"{temp}°F is {new_temp}°C")

else:
    print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")