# Define Player class


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def set_location(self, new_location):
        self.location = new_location
