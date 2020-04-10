import pdb

from room import room
from item import item
from player import Player

from textwrap import TextWrapper

wrapper = TextWrapper(initial_indent='* *  ',
                      subsequent_indent='* *  ',
                      fix_sentence_endings=True)


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Add locations to items

item['lint'].location = room['boh']
item['kopez'].location = room['overlook']
item['insight'].location = room['treasure']


# Add items to locations

room['boh'].inventory.append(item['lint'])
room['overlook'].inventory.append(item['kopez'])
room['treasure'].inventory.append(item['insight'])


# Create player

player = Player(input('player name >>> '), room['outside'])


# Player commands

player_cmds = {
    'n': 'n_to',
    's': 's_to',
    'e': 'e_to',
    'w': 'w_to',
    'i': None,
}


# Print funcs


def prnt_loc():
    print(f'\n********\n\nLocation:   {player.location.name}\n')
    location_str = f'{player.location.description}\n'
    for i in wrapper.wrap(location_str):
        print(i)
    loc_inv_str = [i.name for i in player.location.inventory]
    print(f'\n...items nearby:  {loc_inv_str}')


def prnt_inv():
    player_inv = [i for i in room['boh'].inventory]
    print(f'\n********\n\nInventory:\n')
    for i in player_inv:
        for j in wrapper.wrap(i.name):
            print(j.upper())
        for k in wrapper.wrap(i.description):
            print(k)
        print('\n')
