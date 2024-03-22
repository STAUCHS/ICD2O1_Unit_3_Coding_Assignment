#-------------------------------------------------------------------------
# Name:         Fahrenheit to Celsius
# Purpose:		  Converts the temperature in Fahrenheit to Celsius
# Author:       Chen. C
# Created:      22/03/2024
#-------------------------------------------------------------------------

# Output title
print("** Fahrenheit to Celsius Converter **")

# Get temperature in fahrenheit from user
temp_fahrenheit = int(input("Enter the temperature in Fahrenheit: "))

# Calculate celsius = (5/9)*(F-32)
temp_celsius = (5/9) * (temp_fahrenheit - 32)
temp_celsius = round(temp_celsius)
temp_celsius = int(temp_celsius)

# Output celsius
print("")
print(temp_fahrenheit, "degrees Fahrenheit is", temp_celsius, "degrees Celsius.")