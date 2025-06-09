marks={
"Madhav":10,
"Bipin":15,
"Tek":20
}
# .keys() is function which is used to print the key of the item from the dictionary 
print(marks.keys())
# used to print the value first wala key ho like yo name haru tara yo number wala item chai key ho 

print(marks.values())

marks.update({"Tek":50,"kopila":55})
# here the value of tek will replaced or updated from 20 to 50 so dictionary is mutable , 
# the item is not in the dictionary will be added 
print(marks)
# here pop is used to remove the item form the dictionary 
marks.pop("Tek")
print(marks)
ed = {}  # empty dictionary
print(type(ed))  # prints: <class 'dict'>

ed1 = set()  # empty set
print(type(ed1))  # prints: <class 'set'>
# this is for finding the length of dictionary 
print(len(marks))
