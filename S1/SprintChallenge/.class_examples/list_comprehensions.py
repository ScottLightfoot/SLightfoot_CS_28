# List Comprehensions
#
# Another way of building lists

# Build a list of even numbers the normal way:
evens = []

for num in range(10):
	if num % 2 == 0:  # if num is even
		evens.append(num)  # add to end of list

print(evens)

# Build a list of even numbers using a list comprehension:
evens = [num * 10 for num in range(10) if num % 2 == 0 and num != 6 ]
#        ^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^
#      output            input                filter

print(evens)  # Prints the same as the print on line 8
