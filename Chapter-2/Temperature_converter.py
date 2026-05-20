# Take input in celsius and print its equivalent in Fahrenheit and kelvin.
celsius = float(input("Enter the temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print("output:")
print("The equivalent temperature in Fahrenheit is: ", fahrenheit)
print("The equivalent temperature in Kelvin is: ", kelvin)