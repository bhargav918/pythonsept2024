
#!/usr/bin/python3

celsius = int(input("Enter the Temperature in Celsius :"))   #celsius to fahrenheit
fahrenheit = (1.8 * celsius) + 32
print("Temperature in Fahrenheit :", fahrenheit)


# fahrenheit to celsius

fahrenheit = int(input("Enter the Temperature in fahrenheit :"))
celsius = (fahrenheit - 32) / 1.8
print("Temperature in celsius :", celsius)