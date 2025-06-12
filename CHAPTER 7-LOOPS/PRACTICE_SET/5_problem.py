# printing following starpattern 
#    *
#   ***
#  *****

num=int(input("enter the number:\n"))


for i in range(1,num+1):
    print(" "*(num-i),end="")
    print("*"*(2*i-1))
    

    