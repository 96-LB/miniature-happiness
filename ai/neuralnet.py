import numpy as np

np.random.seed(1)

def sigmoid(Z):
	A = 1/(1+np.exp(np.dot(-1, Z)))

class NeuralNet:
    def __init__(self, layer_dims: list[int]):
        self.L = len(layer_dims)
        self.layer_dims = layer_dims[:]
        self.weights = [None] # first layer has no weights
        self.biases = [None] # first layer has no biases
        for layer in range(1, self.L):
            self.weights.append(np.random.randn(layer_dims[layer - 1], layer_dims(layer))) 
            self.biases.append(np.zeros((layer_dims[layer], 1))) 

    def forward_prop(self, X):
        A = X
        for layer in range(1, self.L):
            Z = np.dot(self.weights[layer], A) + self.biases[layer]
            A = sigmoid(Z)
        return A
