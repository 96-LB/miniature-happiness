import numpy as np
import ai.game, ai.battle
import game.game, game.battle

from random import random

from ai.neuralnet import NeuralNet
from game import MOVE_LEFT, MOVE_RIGHT, MOVE_UP, MOVE_DOWN
from game.battle import FIGHT, RUN


POPULATION_SIZE = 1000
SURVIVORS = 25
assert POPULATION_SIZE // SURVIVORS == POPULATION_SIZE / SURVIVORS
RATIO = POPULATION_SIZE // SURVIVORS
NUM_GENERATIONS = 100

ais: list[list[int, tuple[NeuralNet, NeuralNet]]] = []


def mutate(x):
    MUTATION = 1.0
    return x + np.random.normal(0.0, MUTATION)


def run():
    first_generation()
    for i in range(NUM_GENERATIONS):
        next_generation()
        print(i)
    return ais


def first_generation():
    for i in range(POPULATION_SIZE):
        ais.append([0, (NeuralNet(ai.game.dims), NeuralNet(ai.battle.dims))])


def next_generation():
    play_games()
    ais.sort(reverse=True, key=lambda x: x[0])
    
    for i in range(SURVIVORS):
        for j in range(1, RATIO):
            reproduce(i, i + SURVIVORS * j)


def reproduce(old, new):
    old_game_ai, old_battle_ai = ais[old][1]
    new_game_ai, new_battle_ai = old_game_ai.replicate(), old_battle_ai.replicate()
    ais[new][1] = (new_game_ai, new_battle_ai)
    
    new_game_ai.mutate(mutate, mutate)
    new_battle_ai.mutate(mutate, mutate)

def play_games():
    for i in range(POPULATION_SIZE):
        play_game(ais[i])


def play_game(ai):
    game_ai, battle_ai = ai[1]
    
    game.game.reset_game()
    
    while game.game.is_running:
        if game.battle.is_running:
            inputs = game.battle.get_inputs()
            outputs = forward_prop(inputs, battle_ai)
            output = np.argmax(outputs)
            action = (FIGHT, RUN)[output]
            game.battle.perform_action(action)
        else:
            inputs = game.game.get_inputs()
            outputs = forward_prop(inputs, game_ai)
            output = np.argmax(outputs)
            action = (MOVE_LEFT, MOVE_RIGHT, MOVE_UP, MOVE_DOWN)[output]
            game.game.perform_action(outputs)
    
    ai[0] = game.get_score()
