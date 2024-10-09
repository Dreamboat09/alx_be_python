temp = int(input('Enter the temperature to convert: '))
unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').lower()

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f'{temp} is {celsius}')
    
    convert_to_celsius(fahrenheit)
    
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f'{temp} is {fahrenheit}')
    
    convert_to_fahrenheit(celsius)
    
    
if unit == 'f':
    convert_to_fahrenheit()

elif unit == 'c':
    convert_to_fahrenheit
     
else:
    print('Invalid temperature. Please enter a numeric value.')