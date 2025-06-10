# Write a program which finds out whether a given name is present in a list or not.

names=["bipin","kopila","madhav","anshu"]

user=input("Enter your name\n")

if (user.lower() in names):
    print("Name found in database\n")
        
else:
     print("Name not found in database\n")
        

        