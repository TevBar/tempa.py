import math

Temperature = int(input("Please enter a temperature to convert from F to C: "))

def fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
        celsius = math.ceil(celsius)
        return celsius
    except ValueError:
        print("Error: input should only be a number")
        return None

result = fahrenheit_to_celsius(Temperature)
if result is not None:
    print(f"{Temperature} degrees fahrenheit is {result}")
print("Thank you for using this program for the weather conversion!")