# Write a python function to print first n lines of the following pattern:
# *** n=3
# **
# *

def star(num):
    if num==0:
        return
    print("*" * num)
    star(num-1)

star(5)
