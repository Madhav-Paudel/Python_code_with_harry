# Create an empty dictionary. Allow 4 friends to enter their favorite language
# value and use key as their names. Assume that the names are unique.
languages={}

for x in range(4):
    name=input("Enter you name:\n")
    language=input("Enter your favorite language:\n")
    languages[name]=language

print(languages)