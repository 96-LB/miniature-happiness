import numpy as np

from . import game, fuzzy
import random
import math

FIGHT = 'f'
RUN = 'r'

enemy_health = 0
enemy_damage = 0
enemy_lvl = 0
player_health = 0
player_damage = 0


is_running = False


def get_inputs():
    return np.array([player_health, player_damage, enemy_health, enemy_damage])


def start_battle(player, enemy):
    global player_health, player_damage, enemy_health, enemy_damage, enemy_lvl, is_running
    player_health, player_damage = player
    enemy_health, enemy_damage, enemy_lvl = enemy
    
    is_running = True





def perform_action(action):
    {
        FIGHT: perform_action_fight,
        RUN: perform_action_run,
    }[action]()
# actions

def perform_action_fight():
    global enemy_health

    enemy_health -= player_damage * fuzzy()
    if(enemy_health <= 0):
        game.get_rewards(enemy_lvl * 5 * fuzzy())
        end_battle()
    else:
        enemy_turn()

def perform_action_run():
    if random.randint(0,3) != 0:
        end_battle()
    else:
        enemy_turn()

def enemy_turn():
    global player_health
    
    player_health -= enemy_damage * fuzzy()
    if(player_health <= 0):
        end_battle()
        game.game_over()


def end_battle():
    global is_running

    is_running = False

    
