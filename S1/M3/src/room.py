# Define Room class and create starting rooms with connections


class Room:
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        if inventory is None:
            self.inventory = []

    def add_to_room(self, subj_item):
        try:
            self.inventory.append(subj_item)
        except Exception:
            pass

    def drop_from_room(self, subj_item):
        try:
            self.inventory.remove(subj_item)
        except Exception:
            pass


# Create initial rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     None),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     None),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     None),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     None),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     None),

    'boh': Room("Bag of Holding", "A pocket dimension for all your inventory!",
                     None),
}
