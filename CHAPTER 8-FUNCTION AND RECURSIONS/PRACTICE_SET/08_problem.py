# Write a python function to print multiplication table of a given number.

def print_multiplication_table(number):
	"""Print multiplication table of a given number"""
	for i in range(1, 11):
		print(f"{number} x {i} = {number * i}")

print_multiplication_table(5)
