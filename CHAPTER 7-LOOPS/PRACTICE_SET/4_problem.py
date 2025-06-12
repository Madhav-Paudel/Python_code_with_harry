# Write a program to calculate the factorial of a given number using for loop.
num=int(input("Enter the number:\n"))
fact=1
for i in range(1,num+1):
    fact*=i

    
print(f"The factorial of {num} is {fact}")

