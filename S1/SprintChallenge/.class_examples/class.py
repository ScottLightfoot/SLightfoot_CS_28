class Animal:

    def __init__(self, leg_count=4):   # Constructor, initializes the new obj
        # Print("constructor called!")
        self.leg_count = leg_count
        self.likes_food = True

    def get_leg_count(self):  # getter
        return self.leg_count

    def set_leg_count(self, leg_count):  # setter
        self.leg_count = leg_count


# Objects, AKA instances
cat = Animal()   # Construct a new Animal, Instantiate a new Animal
dog = Animal()   # Construct a new Animal
centipede = Animal(100)


# Make a list of Animals
rabbits = [
    Animal(4),
    Animal(4),
    Animal(4)
]

rabbits[1].leg_count = 3  # leg_count is an "attribute" on the object
print(f"rabbit 0's leg count: {rabbits[0].leg_count}")
print(f"rabbit 1's leg count: {rabbits[1].leg_count}")
print(f"rabbit 2's leg count: {rabbits[2].leg_count}")

# "cat" is an instance of an Animal
# "cat" is an Animal

# print(f"cat's leg count: {cat.leg_count}")

# cat.leg_count = 4

# print(f"cat's leg count: {cat.leg_count}")
# print(f"dog's leg count: {dog.leg_count}")

print(cat.get_leg_count())

cat.set_leg_count(3)

print(cat.get_leg_count())
