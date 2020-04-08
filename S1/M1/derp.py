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

    def read_txt(filepath):
        with open(filepath) as f:
            read_f = f.read()
            print(read_f)


    foo_file = ''

    if Path('../._lambda_repos/intro-python-I/src/foo.txt').exists():
        foo_file = '../._lambda_repos/intro-python-I/src/foo.txt'
    else:
        foo_file = sorted(Path('../').rglob('foo.txt'))[0]
        print('(not operating from root dir, searched/found foo.txt)')

    read_txt(foo_file)
    print('\n\n')
    
    # print(f'No need to f.close()! ~~~ ({f.closed})')

    l1 = "For Sale:"
    l2 = "Baby Shoes,"
    l3 = "never worn."

    six_word_story = [l1, l2, l3]

    txt_path = foo_file.replace('foo.txt', '')
    bar_file = txt_path + 'bar.txt'

    with open(bar_file, 'w+') as f:
        for i in six_word_story:
            f.write(f'{i}\r\n')
    
    read_txt(bar_file)


# * `cal` -- Experiment with module imports and implement a text-based calendar
def cal(month = None, year = None):
    import calendar
    from datetime import datetime as dt

    if month == None: month = dt.now().month
    if year == None: year = dt.now().year

    try:
        c = calendar.TextCalendar(calendar.SUNDAY)
        cal_str = c.formatmonth(year, month)
        print(cal_str)
    except:
        print('cal function expects 2 inputs - (month, year). \nTry again.  Try harder.')

# * `classes` -- Classes and objects
def classes():
    class LatLon:
        
        def __init__(self, lat, lon): 
            self.lat = lat
            self.lon = lon
    
    class Waypoint(LatLon):
        def __init__(self, name, lat, lon):
            self.name = name
            super().__init__(lat, lon)

        def __str__(self):
            wp = f'{self.name}: {self.lat}, {self.lon}'
            return wp

    class Geocache(Waypoint):
        def __init__(self, difficulty, size, name, lat, lon):
            self.difficulty = difficulty
            self.size = size
            super().__init__(name, lat, lon)
        def __str__(self):
            wp = f'{self.name}: {self.lat}, {self.lon} \n diff: {self.difficulty} \n size: {self.size}'
            return wp
    
    new_waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
    print(new_waypoint)

    new_cache = Geocache(1.5, 2, 'Newberry Views', 44052137, -121.41556)
    print(new_cache)

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
