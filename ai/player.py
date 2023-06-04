from dataclasses import dataclass

from .neuralnet import NeuralNet

@dataclass
class Player:
    game_ai : NeuralNet
    battle_ai : NeuralNet
    score : float