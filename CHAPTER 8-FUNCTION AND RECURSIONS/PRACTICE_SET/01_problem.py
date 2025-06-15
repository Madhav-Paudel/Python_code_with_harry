# Write a program using function to find the greatest of the three number. 

def greatest():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    if (a>b and a>c):
        print(f"The greatest number is {a}")
    elif (b>a and b>c):
        print(f"The greatest number is {b}")
    elif (c>a and c>b):
        print(f"The greatest number is {c}")
    else:
        print("enter the correct input")
    
greatest()


