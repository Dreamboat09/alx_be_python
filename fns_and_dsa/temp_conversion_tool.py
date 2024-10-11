FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = float(input('Enter the temperature to convert: '))
unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').lower()

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
   
    return celsius

    
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    
    return fahrenheit
    
    
if unit == 'c':
    fahrenheit = convert_to_fahrenheit(temp)
    print(f'{temp}°C is {fahrenheit}°F')

elif unit == 'f':
    celsius = convert_to_celsius(temp)
    print(f'{temp}°F is {celsius}°C')
    
else:
    print('Invalid temperature. Please enter a numeric value.')