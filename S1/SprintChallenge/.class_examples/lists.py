# Arrays in Python are called lists

a = [11, 22, 33, 44]

# Print every element in list 'a':
for i in a:
    print(i)

# Print 0 to 4
for i in range(5):
    print(i)

# Print element index AND element for each element in a:
for i, foo in enumerate(a):
    print(i, foo)
