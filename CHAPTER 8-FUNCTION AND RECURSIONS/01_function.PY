# This is know as function definition 
def avg():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))

    average = (a + b + c) / 3
    return average
# this is known as function calling 

a=avg()
print(a)

