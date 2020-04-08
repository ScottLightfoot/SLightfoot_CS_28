# * `hello` -- Hello world
def hello(x = "Hello, world!"):
    print('Hello, world')

# * `bignum` -- Print some big numbers
def bignum(x = 2, y = 65536, z = "sci-notation"):
    bn = x**y

    if z == "sci-notation":
        count = 0
        while bn >= 10:
            count += 1
            bn //= 10
        mant = x**y / 10**count
        print(f'{mant:.{5}f}e{count:+d}')
        # print('{0:.{1}f}e{2:+d}'.format(mant, 3,count))
        # print(str(f'{x**65536:E}'))
    else:
        print(str(x**65536))

# * `datatypes` -- Experiment with type conversion
def datatypes(x = 5, y = '7'):
    print(f'as a string: \n {str(x)}{str(y)}')
    try:
        print(f'as an int: \n {int(x) + int(y)}')
    except:
        print('you sure both of those could be ints??')

# * `modules` -- Learn to import from modules
def modules():
    import sys, os

    for arg in dir(sys):
        print(f'argv: {arg}')
        
    print(f'Platform: {sys.platform}')
    print(f'PythonVer: {sys.version}')

    print(f'ProcessID: {os.getpid()}')
    print(f'WorkingDir: {os.getcwd()}')
    print(f'LoginName: {os.getlogin()}')

# * `printing` -- Formatted print output
def printing(x = 10, y = 2.24552, z = 'I like turtles!'):
    # https://www.youtube.com/watch?v=CMNry4PE93Y

    print('Using f-string:')
    print(f'x is {x}, y is {y:.2f}, z is {z}')
    print('Using string modulo:')
    print('x is %2d, y is %1.2f, z is %s' %(x, y, z))
    print('Using .format()')
    print('x is {0}, y is {2:.2f}, z is {1}'.format(x,z,y))

# * `lists` -- Python's version of arrays
def lists(x = [1, 2, 3], y = [8, 9, 10]):
    print(f'x: {x}\n')
    
    x.append(4)
    print(f'x: {x}\n')
    
    x += y
    print(f'x: {x}\n')
    
    x.remove(8)
    print(f'x: {x}\n')
    
    x.insert(-1, 99)
    print(f'x: {x}\n')
    
    print(f'length of list x: {len(x)}')
    
    print([i * 1000 for i in x])
    
# * `tuples` -- Immutable lists typically for heterogenous data
def tuples(t = (1,2,5,7,99), u = (1)):

    # as provided in the assignment, a tuple cannot be assigned.
    # If provided this way (i.e. single element) a conversion can be done --
    
    def print_tuple(x):
        if type(x) == type(tuple()):
            for i in x: print(i)
        else:
            try:
                for i in tuple([x]): print(i)
            except:
                print('you sure that\'s tuple-able? (tupleable is a word now)')

    print_tuple(t)
    print_tuple(u)

# * `slices` -- Accessing parts of lists
def slices(a = [2, 4, 1, 7, 9, 6], s = 'Hello, world!'):
    print(a[1])
    print(a[-2])
    print(a[-3:])
    
    if len(a) % 2 == 0:
        b = len(a)//2
        print(a[b], ',', a[b+1])
    else:
        print(a[b+1])
    
    print(a[1:])
    print(a[:-1])
    print(s[7:12])


# * `comprehensions` -- List comprehensions
def comprehensions(y=[], a = ['foo', 'bar', 'baz']):
    y = []
    for i in range(1,6): y.append(i)
    print(y)

    y = []
    for i in range(10): y.append(i**3)
    print(y)

    y = []
    for i in a: y.append(i.upper())
    print(y)

    y = []
    x = input('enter comma-separated vals: ')
    try:
        x = x.replace(' ', '').split(',') 
    except:
        print('what\'d you try to give me just now??!')
    for i, val in enumerate(x):
        if i % 2 == 0:
            try:
                y.append(int(val))
            except:
                y.append(val)
    print(y)

# * `dictionaries` -- Dictionaries
def dictionaries():
    waypoints = [
        {
            "lat": 43,
            "lon": -121,
            "name": "a place"
        },
        {
            "lat": 41,
            "lon": -123,
            "name": "another place"
        },
        {
            "lat": 43,
            "lon": -122,
            "name": "a third place"
        }
    ]
    new_point = {
        "lat": 0,
        "lon": 0,
        "name": "nowhere"
    }
    waypoints.append(new_point)

    for i in waypoints:
        if i["name"] == "a place":
            i["lon"] = -130
            i["name"] = "not a real place"
        for key,val in i.items(): print(key, val)

# * `functions` -- Functions
def functions():
    num = input("Enter a number: ")

    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False
    
    try:
        num = int(num)
        if is_even(num):
            print("Even!")
        else:
            print("Odd!")
    except:
        print(f'I SAID A NUMBER!!! WHAT AM I SUPPOSED TO DO WITH "{num.upper()}"')

# * `args` -- Arguments and Keyword Arguments
def args():
    def f1(p0_var, p1_var):
        try:
            return p0_var + p1_var
        except:
            return "ints & | floats only!!"
            
    print(f1(1, 2))

    def f2(*ints):
        if type(ints[0]) == type(list()):
            ints = tuple(ints[0])
        return(sum(ints))

    print(f2(1))                    # Should print 1
    print(f2(1, 3))                 # Should print 4
    print(f2(1, 4, -12))            # Should print -7
    print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

    # How do you have to modify the f2 call below to make this work?
    #  --- I don't???

    a = [7, 6, 5, 4]
    
    print(f2(a))    # Should print 22

    def f3(*x):
        if len(x) == 1:
            return sum(x,1)
        else:
            return sum(x)


    print(f3(1, 2))  # Should print 3
    print(f3(8))     # Should print 9

    def f4(**kwargs):
        # pdb.set_trace()
        for key,val in kwargs.items():
            print(f'Key: {key}, val: {val}')
    
    f4(a=12, b=30)
    f4(city="Berkeley", population=121240, founded="March 23, 1868")

    d = {
        "monster": "goblin",
        "hp": 3
    }
    
    f4(**d)

# * `scopes` -- Global, Local, and Non-Local scope
def scopes():
    x = 12

    def change_x():
        nonlocal x
        x = 99

    print(f'before change x: {x}')
    change_x()
    print(f'after change x: {x}')

    def outer():
        y = 120

        def inner():
            nonlocal y
            y = 999


        print(f'before inner(): {y}')
        inner()
        print(f'after inner(): {y}')
        


    outer()

# * `file_io` -- Read and write from files
def file_io():
    from pathlib import Path

    foo_file = ''

    if Path('./intro-python-I/src/foo.txt').exists():
        foo_file = './intro-python-I/src/foo.txt'
    else:
        foo_file = sorted(Path().rglob('foo.txt'))[0]
        print('(not operating from root dir, searched/found foo.txt)')

    with open(foo_file) as f:
        read_f = f.read()
        print(read_f)
    
    print(f'No need to f.close()! ~~~ ({f.closed})')

    l1 = "For Sale:"
    l2 = "Baby shoes,"
    l3 = "never worn."



# # Open up a file called "bar.txt" (which doesn't exist yet) for
# # writing. Write three lines of arbitrary content to that file,
# # then close the file. Open up "bar.txt" and inspect it to make
# # sure that it contains what you expect it to contain

# # YOUR CODE HERE


# #######

# # * `cal` -- Experiment with module imports and implement a text-based calendar
# def cal():
#     pass

# """
# The Python standard library's 'calendar' module allows you to
# render a calendar to your terminal.
# https://docs.python.org/3.6/library/calendar.html

# Write a program that accepts user input of the form
#   `14_cal.py [month] [year]`
# and does the following:
#  - If the user doesn't specify any input, your program should
#    print the calendar for the current month. The 'datetime'
#    module may be helpful for this.
#  - If the user specifies one argument, assume they passed in a
#    month and render the calendar for that month of the current year.
#  - If the user specifies two arguments, assume they passed in
#    both the month and the year. Render the calendar for that
#    month and year.
#  - Otherwise, print a usage statement to the terminal indicating
#    the format that your program expects arguments to be given.
#    Then exit the program.

# Note: the user should provide argument input (in the initial call to run the file) and not 
# prompted input. Also, the brackets around year are to denote that the argument is
# optional, as this is a common convention in documentation.

# This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
# print out a calendar for April in 2015, but if you omit either the year or both values, 
# it should use today’s date to get the month and year.
# """

# import sys
# import calendar
# from datetime import datetime


# #######



# # * `classes` -- Classes and objects
# def classes():
#     pass

# # Make a class LatLon that can be passed parameters `lat` and `lon` to the
# # constructor

# # YOUR CODE HERE

# # Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# # constructor. It should inherit from LatLon. Look up the `super` method.

# # YOUR CODE HERE

# # Make a class Geocache that can be passed parameters `name`, `difficulty`,
# # `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# # YOUR CODE HERE

# # Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# # YOUR CODE HERE

# # Without changing the following line, how can you make it print into something
# # more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# # Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# # YOUR CODE HERE

# # Print it--also make this print more nicely
# print(geocache)

# #######



def sandbox(list, passes):
    
    if passes == 1:
        next_num = 1
    else:
        next_num = (passes-2) * 4 + 3
    
    step = 2**(passes)

    indxs = []

    while next_num < len(list):
        indxs.append(next_num)
        next_num += step
    
    return [list[i] for i in indxs]
