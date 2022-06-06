import numpy as np


def MSE(predicted, target):
    return np.sum(np.power((target - predicted), 2))


def Sigmoid(x):
    return 1 / (1 + np.exp(-x))


def HBTangents(x):
    return 2 * Sigmoid(2 * x) - 1


def ReLU(x):
    return np.maximum(0, x)


def Constant(x):
    return x


def DerivMSE(predicted, target):
    return 2 * (target - predicted) / predicted.size


def DerivSigmoid(x):
    return Sigmoid(x) * (1 - Sigmoid(x))


def DerivHBTangents(x):
    return 1 - np.power(HBTangents(x), 2)


def DerivReLU(x):
    return np.heaviside(x, 0)


def DerivConstant(x):
    return 1


def DefineDeriv(activation):
    switch = {
        ReLU: DerivReLU,
        Sigmoid: DerivSigmoid,
        HBTangents: DerivHBTangents,
        Constant: DerivConstant,
        MSE: DerivMSE
    }
    return switch.get(activation, "Wrong input function\n"
                                  "Usage: ReLU, Sigmoid, HBTangents, Constant or MSE")
