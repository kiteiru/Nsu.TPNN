import numpy as np

from utils import DefineDeriv


class NetworkLayer:
    def __init__(self, previousDim, currentDim, activationFunction):
        self.inputs = None
        self.linearCombination = None
        self.weights = np.random.uniform(-0.6, 0.6, (previousDim, currentDim))
        self.activationFunction = activationFunction

    def ForwardPropagation(self, inputs):
        self.inputs = inputs
        self.linearCombination = np.dot(self.inputs, self.weights)
        return self.activationFunction(self.linearCombination)

    def BackwardPropagation(self, backwardError, lr):
        backwardError = DefineDeriv(self.activationFunction)(self.linearCombination) * backwardError
        self.weights -= lr * np.dot(self.inputs.T, backwardError)
        delta = np.dot(backwardError, self.weights.T)
        return delta
