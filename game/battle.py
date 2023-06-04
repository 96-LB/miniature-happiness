FIGHT = 'f'
RUN = 'r'



def start_battle(player, enemy):
    # resets the battle
    ...


def perform_action(action):
    {
        FIGHT: lambda: print('Fighting...'),
        RUN: lambda: print('Running fast...'),
    }[action]()


# actions