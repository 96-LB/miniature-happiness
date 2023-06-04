import numpy as np
import ai.game, ai.battle
import game, game.battle

from random import random

from . import forward_prop, generate_random
from game import MOVE_LEFT, MOVE_RIGHT, MOVE_UP, MOVE_DOWN
from game.battle import FIGHT, RUN


POPULATION_SIZE = 1000
SURVIVORS = 25
assert POPULATION_SIZE // SURVIVORS == POPULATION_SIZE / SURVIVORS
RATIO = POPULATION_SIZE // SURVIVORS
NUM_GENERATIONS = 100

ais: list = []


def mutate():
    MUTATION = 0.05
    return MUTATION * (random() - 0.5)


def first_generation():
    for i in range(POPULATION_SIZE):
        ais.append([0, (generate_random(ai.game.dims), generate_random(ai.battle.dims))])


def next_generation():
    play_games()
    ais.sort(reverse=True, key=lambda x: x[0])
    
    for i in range(SURVIVORS):
        for j in range(1, RATIO):
            reproduce(i, i + SURVIVORS * j)


def reproduce(old, new):
    old_game_ai, old_battle_ai = ais[old][1]
    new_game_ai, new_battle_ai = ais[new][1]
    
    for i in range(len(ai.game.dims) - 1):
        # deal with weight
        for j in range(old_game_ai[0].shape[0]):
            for k in range(old_game_ai[0].shape[1]):
                new_game_ai[2 * i][j][k] = old_game_ai[2 * i][j][k] + mutate()
        
        # deal with biases
        for j in range(old_game_ai[1].shape[0]):
            new_game_ai[2 * i + 1][j] = old_game_ai[2 * i + 1][j] + mutate()
    
    for i in range(len(ai.battle.dims) - 1):
        # deal with weight
        for j in range(old_battle_ai[0].shape[0]):
            for k in range(old_battle_ai[0].shape[1]):
                new_battle_ai[2 * i][j][k] = old_battle_ai[2 * i][j][k] + mutate()
        
        # deal with biases
        for j in range(old_battle_ai[1].shape[0]):
            new_battle_ai[2 * i + 1][j] = old_battle_ai[2 * i + 1][j] + mutate()


def play_games():
    for i in range(POPULATION_SIZE):
        play_game(ais[i])


def play_game(ai):
    game_ai, battle_ai = ai[1]
    
    game.reset_game()
    
    while game.is_running:
        if game.is_running:
            inputs = game.battle.get_inputs()
            outputs = forward_prop(inputs, battle_ai)
            output = np.argmax(outputs)
            action = (FIGHT, RUN)[output]
            game.battle.perform_action(action)
        else:
            inputs = game.get_inputs()
            outputs = forward_prop(inputs, game_ai)
            output = np.argmax(outputs)
            action = (MOVE_LEFT, MOVE_RIGHT, MOVE_UP, MOVE_DOWN)[output]
            game.perform_action(outputs)
    
    ai[0] = game.get_score()
