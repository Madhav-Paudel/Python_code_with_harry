# Write a program to input eight numbers from the user and display all the unique
# numbers (once).

numbers=set()

for x in range(8):
    number=int(input("Enter number\n"))
    numbers.add(number)

print(numbers)
