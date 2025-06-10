# 7. Write a program to find out whether a given post is talking about "Harry" or not.
post=input("enter sentences:\n")

if "Harry".lower() in post.lower():
    print("This post is talking about harry\n")
else:
    print("This post is not talking about harry\n")
