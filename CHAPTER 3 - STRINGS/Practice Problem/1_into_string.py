
# We can primarily write a string in these three ways.
# a ='Madhav' # Single quoted string
# print(a)
# b = "Madhav"# Double quoted string
# print(b)
# c ='''Madhav'''# Triple quoted string
# print(c)

# here is string slicing 
name="Madhav paudel"
# if i want only madhav then 

first_name=name[0:6] #here[starting=0;end=6]

print(first_name)
# again if i want only the last name then 
last_name=name[7:13]

print(last_name)
# above all example are of positive slicing now turn for positive slicing 

print(name[-11:-5])
print(name[5:11])

# name1="harry"
# print(name1[-4:-1])
# print(name1[1:4])
test="Madhav"
print(test[-5:-1])

print(test[1:5])
# slicing 
a="0123456789"
a1=a[0:5:3]
print(f"{a1}")

