# Inheritance

"""
Inheritance diagram:

[Animal] <- [Dog]
   ^
   |
 [Cat] <- [Tabby]
"""


class Animal:

    def __init__(self, leg_count):
        print("Animal constructor")
        self.leg_count = leg_count

    def make_sound(self):
        print("[generic animal noise]")


class Dog(Animal):
    # Dog inherits from Animal, dog is an animal. (is-a relationship)

    # Override the make_sound method
    def make_sound(self):
        super().make_sound()
        print("Arf")


class Cat(Animal):
    def __init__(self, tail_length):
        # Call the constructor of Animal with 4 legs
        super().__init__(leg_count)
        self.tail_length = tail_length


class Tabby(Cat):
    def __init__(self):
        # Call the constructor of Cat with tail 8
        super().__init__(8)


cat = Cat(8)
dog = Dog()

cat.make_sound()
dog.make_sound()

print(cat.leg_count)
