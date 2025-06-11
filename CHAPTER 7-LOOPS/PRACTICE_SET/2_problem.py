# Write a program to greet all the person names stored in a list 'I' and which starts
# with S.
i=["Harry", "Soham", "Sachin", "Rahul"]

for name in i:
    if name.startswith("S"):
        print(f"Hello {name}")
