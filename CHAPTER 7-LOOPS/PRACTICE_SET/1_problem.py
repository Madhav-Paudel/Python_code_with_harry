# Write a program to print multiplication table of a given number using for loop.
num=int(input("enter  any number\n"))
for i in range(1,11):
    a=num*i
    print(f"{num}x{i}={a}")
