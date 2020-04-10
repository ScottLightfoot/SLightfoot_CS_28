from textwrap import TextWrapper

wrapper = TextWrapper(initial_indent='* *  ',
                      subsequent_indent='* *  ',
                      fix_sentence_endings=True)


# Create directions for player travel

player_cmds = {
    'n': 'n_to',
    's': 's_to',
    'e': 'e_to',
    'w': 'w_to',
    'i': None,
    'take': 'add_to_inventory',
    'drop': 'remove_from_inventory'
    }


def prnt_loc(player):
    print(f'\n********\n\nLocation:   {player.location.name}\n')
    location_str = f'{player.location.description}\n'
    for i in wrapper.wrap(location_str):
        print(i)
    print(f'\n...items nearby:  {player.location.inventory.name}')


def prnt_inv(player):
    player_inv = [i for i in room['boh'].inventory]
    print(f'\n********\n\nInventory:\n')
    for i in player_inv:
        print(f'{i.name} - {i.description}')

# def get_item(subj_item):
#         try:
#             player.inventory.append(subj_item)
#             item[subj_item].location = room['boh']
#             room[self.location].remove_item(subj_item)
#             return True
#         except Exception:
#             pass
