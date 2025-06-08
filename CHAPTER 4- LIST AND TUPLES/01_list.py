examples=["apple","Ball","Cat",1,5,False,"dog"]
print(examples)

for example in examples:
    print(example)
# we can add any thing to the and position of the list.

examples[5]="Hello"
# here False is replace by the word Hello 
# string are immutable but as we can see the list is mutable 

print(examples)


# slicing in the list is similar as the slicing in the string 
print(examples[4:7])

