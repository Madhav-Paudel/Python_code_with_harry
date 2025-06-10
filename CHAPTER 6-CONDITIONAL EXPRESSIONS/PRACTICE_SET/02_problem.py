# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

subject1=int(input("Enter your marks in subject 1:\n"))
subject2=int(input("Enter your marks in subject 2:\n"))
subject3=int(input("Enter your marks in subject 3:\n"))

total_percentage=(100*(subject1+subject2+subject3))/300

if total_percentage>= 40 and subject1>=33 and subject2>=33 and subject3>=33:
    print(f"You are pass and your percentage is {total_percentage}%")
else:
    print(f"You are fail and your percentage is {total_percentage}%")



