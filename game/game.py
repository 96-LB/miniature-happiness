import numpy as np

from . import fuzzy, battle
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
player_maxHealth = 20
player_attack = 1
turns = 0

def get_inputs():
    return np.array([distance, level])




def reset_game():
    # resets the game
    global is_running, distance, level, exp, player_maxHealth, player_attack, turns
    distance = 0
    level = 1
    exp = 0
    player_maxHealth = 20
    player_attack = 1
    battle.end_battle()
    is_running = True
    turns = 15

def perform_action(action):
    global turns
    
    if battle.is_running:
        raise Exception('You are in a battle!')
    
    if turns <= 0:
        game_over()
    else:
        {
            MOVE_LEFT: perform_action_left,
            MOVE_RIGHT: perform_action_right,
            MOVE_UP: perform_action_up,
            MOVE_DOWN: perform_action_down,
        }[action]()
        random_battle_chance()
        


def perform_action_left():
    global distance
    if distance > 0:
        distance += -1

def perform_action_right():
    global distance
    distance += 1



def perform_action_up():
    ...

def perform_action_down():
    ...

# other actions

def get_score() -> float:
    
    if distance // 5 + 1 < level:
        return (distance // 5 + 1) * (distance // 5 + 1) * 10
    return exp




def random_battle_chance():
    random_number = random.randint(0, 4)
    if random_number == 0:
        create_enemy()

def create_enemy():
    global distance, player_maxHealth, player_attack, turns
    enemy_level = distance // 5 + 1
    enemy_health = enemy_level * 10 * fuzzy()
    enemy_attack = enemy_level * fuzzy()
    
    battle.start_battle((player_maxHealth, player_attack), (enemy_health, enemy_attack, enemy_level))
    turns -= 1

#every 5 distace, enemies get stronger

def level_up():
    global player_maxHealth, player_attack, level
    player_attack += 1
    player_maxHealth += 10
    level += 1


def get_rewards(amt):
    global exp

    exp += amt
    if(exp >= level * level * 10):
        level_up()

def game_over():
    global is_running

    is_running = False