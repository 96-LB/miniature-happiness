import numpy as np

np.random.seed(1)

def sigmoid(Z):
	A = 1/(1+np.exp(np.dot(-1, Z)))

class NeuralNet:
    def __init__(self, layer_dims, weights = None, biases = None):
        self.L = len(layer_dims)
        self.layer_dims = layer_dims[:]

        if weights is None:
            self.weights = [None] # first layer has no weights
            for layer in range(1, self.L):
                self.weights.append(np.random.randn(layer_dims[layer - 1], layer_dims(layer))) 
        else:
            self.weights = weights[:]

        if biases is None:
            self.biases = [None] # first layer has no biases
            for layer in range(1, self.L):
                self.biases.append(np.zeros((layer_dims[layer], 1))) 
        else:
            self.biases = biases[:]

    def forward_prop(self, X):
        A = X
        for layer in range(1, self.L):
            Z = np.dot(self.weights[layer], A) + self.biases[layer]
            A = sigmoid(Z)
        return A
