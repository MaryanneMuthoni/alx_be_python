# Create a Python script named temp_conversion_tool.py.
# This script will define functions to convert temperatures between Celsius and Fahrenheit 
# Demonstrating the use of global variables to store conversion factors that are accessible within functions.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

temperature = float(input("Enter the temperature to convert: "))
check = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if check == "F":
    result = convert_to_celsius(temperature)
    print(f"{temperature}°F is {result}°C")
elif check == "C":
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")
