# Write a program to accept marks of 6 student and display them in sorted order 

marks=[]

for x in range(6):
    mark=int(input("Enter the marks of student:\n"))
    marks.append(mark)

marks.sort()
print(marks)