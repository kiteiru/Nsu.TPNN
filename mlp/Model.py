from NetworkLayer import NetworkLayer
from utils import HBTangents, Sigmoid, ReLU, Constant, MSE, DefineDeriv


class Model:
    def __init__(self):
        self.first = NetworkLayer(1, 50, HBTangents)
        self.second = NetworkLayer(50, 150, Sigmoid)
        self.third = NetworkLayer(150, 15, ReLU)
        self.output = NetworkLayer(15, 1, Constant)

        self.architecture = []
        self.architecture.append(self.first)
        self.architecture.append(self.second)
        self.architecture.append(self.third)
        self.architecture.append(self.output)

        self.costFunction = MSE

    def TrainNetwork(self, dataset, target, lr, epochNum):
        epochsErrors = []
        for epoch in range(epochNum):
            error = 0
            for sample, targetValue in zip(dataset, target):
                inputs = sample
                for layer in self.architecture:
                    inputs = layer.ForwardPropagation(inputs)
                error += self.costFunction(targetValue, inputs)
                backwardError = DefineDeriv(self.costFunction)(targetValue, inputs)
                for layer in reversed(self.architecture):
                    backwardError = layer.BackwardPropagation(backwardError, lr)
            epochsErrors.append(error / len(dataset))
            print(f"Epoch #{epoch + 1} is finished: error equals {round(epochsErrors[epoch], 6)}")
        return epochsErrors

    def PredictValues(self, inputValue):
        for layer in self.architecture:
            inputValue = layer.ForwardPropagation(inputValue)
        return [inputValue]

