# Write a program to detect the double space in the string.
string1="My name is Madhav"

a = string1.find("  ")
if a==-1:
    print("There is no Double Space")
else:
    print("There is Double Space")
    print(string1.replace("  "," "))


