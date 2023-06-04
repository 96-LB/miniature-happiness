import numpy as np

def generate_random(dims):
    params = []
    for i in range(len(dims) - 1):
        # generate weights
        params.append(np.random.random((dims[i], dims[i + 1])))
        # generate biases
        params.append(np.random.random((dims[i + 1])))
    return params


def sigmoid(x):
    return 1/(1 + np.exp(np.dot(-1, x)))


def forward_prop(inputs, params):
    layer = inputs
    for weights, biases in params:
        layer = np.dot(layer, weights) + biases
        layer = sigmoid(layer)
    
    return layer
