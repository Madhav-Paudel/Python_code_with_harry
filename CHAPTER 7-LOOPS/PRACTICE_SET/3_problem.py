#  Write a program to find the sum of first n natural numbers using while loop.

num=int(input("enter number:\n"))
i=1
number=0

while(i<=num):
    number=((i*(i+1))/2)
    i+=1
print(f"The sum of first {num} is {number}")