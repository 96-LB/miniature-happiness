import numpy as np

from . import battle
import random
import math


MOVE_RIGHT = 'r'
MOVE_LEFT = 'l'
MOVE_UP = 'u'
MOVE_DOWN = 'd'


is_running = False
distance = 0
level = 1
exp = 0
player_maxHealth = 3
player_attack = 3
turns = 0

def get_inputs():
    return np.array([distance, 0, level])




def reset_game():
    # resets the game
    global is_running, distance, level, exp, player_maxHealth, player_attack, turns
    distance = 0
    level = 1
    exp = 0
    player_maxHealth = 3
    player_attack = 3
    battle.end_battle()
    is_running = True
    turns = 100

def perform_action(action):
    global turns
    
    if battle.is_running:
        raise Exception('You are in a battle!')
    
    {
        MOVE_LEFT: perform_action_left,
        MOVE_RIGHT: perform_action_right,
        MOVE_UP: perform_action_up,
        MOVE_DOWN: perform_action_down,
    }[action]()

    turns -= 1
    if turns <= 0:
        game_over()


def perform_action_left():
    global distance
    if distance > 0:
        distance += -1
        random_battle_chance()

def perform_action_right():
    global distance
    distance += 1
    random_battle_chance()



def perform_action_up():
    ...

def perform_action_down():
    ...

# other actions

def get_score() -> float:
    return exp



def random_battle_chance():
    random_number = random.randint(0, 4)
    if random_number == 0:
        create_enemy()

def create_enemy():
    global distance, player_maxHealth, player_attack
    enemy_level = math.floor(distance/5) + 1
    enemy_total_stats = enemy_level * 3
    enemy_health = round((enemy_total_stats/2) + (enemy_total_stats/2 * ((random.randint(-8,8)/32))))
    enemy_attack = enemy_total_stats - enemy_health
    
    battle.start_battle((player_maxHealth, player_attack), (enemy_health, enemy_attack, enemy_level))

#every 5 distace, enemies get stronger

def level_up():
    global player_maxHealth, player_attack
    random_number = random.randint(0,1)
    if(random_number == 0):
        player_attack += 2
        player_maxHealth += 1
    elif(random_number == 1):
        player_attack += 1
        player_maxHealth += 2


def get_rewards(amt):
    global exp

    exp += amt
    if(exp > level * level * 10):
        level_up()

def game_over():
    global is_running

    is_running = False