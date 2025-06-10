# write a program to find the greatest of 4 number enter by the user 

 
a=int(input("Enter first number:\n"))
b=int(input("Enter second number:\n"))
c=int(input("Enter third number:\n"))
d=int(input("Enter forth number:\n"))

if a>b and a>c and a>d:
    print(f"{a} is the greatest number\n")
elif b>a and b>c and b>d:
    print(f"{b} is the greatest number\n")
elif c>a and c>b and c>d:
    print(f"{c} is the greatest number\n")
else:
    print(f"{d} is the greatest number\n")



    
 