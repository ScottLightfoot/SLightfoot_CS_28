# Define Item class and create starting items


class Item:
    def __init__(self, name, description, weight_class, location):
        self.name = name
        self.description = description
        self.weight_class = weight_class
        if location is None:
            self.location = ''
    
    def update_location(self, new_loc):
        self.location = new_loc


# Create initial items

item = {
    'kopez':  Item(
        'kopez',
        'Knock-off PEZ Dispenser - Shit PEZ dispenser of a character named "Buck\'s Bunny"... (and of course, it\'s empty)',
        0,
        None),
    'lint': Item(
        "lint",
        "In a world without pockets, where could this have come from?",
        1,
        None),
    'insight': Item(
        "insight",
        "A crushing, unfiltered comprehension of reality",
        500,
        None),
}
