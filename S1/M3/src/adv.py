from world import *

while True:
    player_input = input(
        f'\n********\n\nSo, {player.name}, what now?\n>>> '
        ).lower()

    if player_input == 'q':
        break

    if player_input.split()[0] in ['get', 'drop']:
        action = player_input.split()[0]
        subj_item = player_input.split()[1]
        if action == 'get':
            try:
                room['boh'].add_to_room(item[subj_item])
                player.location.drop_from_room(item[subj_item])
                print(f'{item[subj_item].name} added to your inventory!')
            except Exception:
                print('you sure that\'s here to procure??')
        if action == 'drop':
            try:
                room['boh'].drop_from_room(item[subj_item])
                player.location.add_to_room(item[subj_item])
                print('yeah... no big. you just go ahead & litter.  \n\
                      (you\'re a monster.)')
            except Exception:
                print('I get it, spelling is hard.')

    elif player_input not in player_cmds:
        print('\n********\n\n')
        print('n | s | e | w | i | get | drop | (or "q" to quit)')
        print('\n********\n\n')

    elif player_input == 'i':
        prnt_inv()

    else:
        try:
            heading = player_cmds[player_input]
            new_loc = getattr(player.location, heading)
            player.set_location(new_loc)
            prnt_loc()
        except Exception:
            print('\n********\n\nyou walked into a wall.  hurt, didn\'t it?')
