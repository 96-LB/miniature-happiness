import numpy as np
import ai.game, ai.battle
import game.game, game.battle

from .neuralnet import NeuralNet
from .player import Player
from game.game import MOVE_LEFT, MOVE_RIGHT, MOVE_UP, MOVE_DOWN
from game.battle import FIGHT, RUN


POPULATION_SIZE = 1000
SURVIVORS = 25
assert POPULATION_SIZE // SURVIVORS == POPULATION_SIZE / SURVIVORS
RATIO = POPULATION_SIZE // SURVIVORS
NUM_GENERATIONS = 100

ais: list[Player] = []


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
        ais.append(Player(NeuralNet(ai.game.dims), NeuralNet(ai.battle.dims), 0))


def next_generation():
    play_games()
    ais.sort(reverse=True, key=lambda x: x.score)
    
    for i in range(SURVIVORS):
        for j in range(1, RATIO):
            reproduce(ais[i], ais[i + SURVIVORS * j])


def reproduce(old: Player, new: Player):
    new.game_ai = old.game_ai.replicate()
    new.battle_ai = old.battle_ai.replicate()
    
    new.game_ai.mutate(mutate, mutate)
    new.battle_ai.mutate(mutate, mutate)


def play_games():
    for i in range(POPULATION_SIZE):
        play_game(ais[i])


def play_game(ai):
    game.game.reset_game()
    
    while game.game.is_running:
        if game.battle.is_running:
            inputs = game.battle.get_inputs()
            outputs = ai.battle_ai.forward_prop(inputs)
            output = np.argmax(outputs)
            action = (FIGHT, RUN)[output]
            game.battle.perform_action(action)
        else:
            inputs = game.game.get_inputs()
            outputs = ai.game_ai.forward_prop(inputs)
            output = np.argmax(outputs)
            action = (MOVE_LEFT, MOVE_RIGHT, MOVE_UP, MOVE_DOWN)[output]
            game.game.perform_action(action)
    
    ai.score = game.game.get_score()
