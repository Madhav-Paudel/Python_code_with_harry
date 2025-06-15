# Write a recursive function to calculate the sum of first n natural numbers.

def sum(num):
    if num==0 or num==1:
        return num 
    else:
        return num +sum(num-1)

a=sum(int(input("enter the number:\n")))
print(a)


