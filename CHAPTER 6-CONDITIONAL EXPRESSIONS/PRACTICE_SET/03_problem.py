# A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". Write a program
# to detect these spams.

keywords=["Make a lot of money", "buy now", "subscribe this", "click this"]

comment= input("enter your message:\n")

for keyword in keywords:
    if keyword==comment:
        print("This is spam comment\n")
        break

    else:
        print("This is valid comment:\n")
        break


