# Write a program using function to convert the celsius into fahrenheit.

def temp(a):
    calculate=(a*9/5)+32
    return calculate

a=temp(int(input("enter the temperate in fahrenheit:\n")))
print(f"the temperature in celsius is {a}")

