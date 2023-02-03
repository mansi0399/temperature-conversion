ask = input("Enetr in which form you want a temperature:")
if ask == "F":
    temp = float(input("Enter a temperature in Fahrenheit: "))
    celsius = (temp - 32)*5/9
    print(f"{temp} in Fahrenheit is equal to {celsius} in Celsius: ")
elif ask == "C":
    temp = float(input("Enter a temperature in Celsius: "))
    fahrenheit = (temp * 1.8)+32
    print(f"{temp} in Celsius is equal to {fahrenheit} in Fahrenheit: ")
else:
    print("Invalid input BRO!")