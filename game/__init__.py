MOVE_RIGHT = 'r'
MOVE_LEFT = 'l'
MOVE_UP = 'u'
MOVE_DOWN = 'd'


is_battling = False
is_game_over = True

def reset_game():
    # resets the game
    global is_battling, is_game_over
    
    is_battling = False
    is_game_over = False

def perform_action(action):
    if is_battling:
        raise Exception('You are in a battle!')
    
    {
        MOVE_LEFT: perform_action_left,
        MOVE_RIGHT: lambda: print('Moving right...'),
        MOVE_UP: lambda: print('Moving up...'),
        MOVE_DOWN: lambda: print('Moving down...'),
    }[action]()


def perform_action_left():
    ...

# other actions

def get_score() -> float:
    ...
