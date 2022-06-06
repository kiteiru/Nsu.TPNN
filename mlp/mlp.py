import numpy as np
from Model import Model
import matplotlib.pyplot as plt


def InitializeData():
    dataset = np.linspace(-1.5 * np.pi, 1.5 * np.pi, 160)
    target = [4 * np.sin(x) for x in dataset]
    return dataset, target


def DrawPlots(epochNum, epochErrors, dataset, target, predictions):
    fig = plt.figure()

    plt.scatter([i for i in range(epochNum)], epochErrors, s=10, color='#ff7373')
    plt.legend(["error"], bbox_to_anchor=(0, 1, 1, 0), loc="lower center", ncol=2)
    plt.show()
    fig.savefig('plots/error.png', dpi=150)

    fig = plt.figure()
    plt.scatter(dataset, target, s=10, color='#8d4dca')
    plt.scatter(dataset, predictions, s=10, color='#ff9c00')
    plt.legend(["target", "predicted"], bbox_to_anchor=(0, 1, 1, 0), loc="lower center", ncol=2)
    plt.show()
    fig.savefig('plots/predictions.png', dpi=150)


if __name__ == '__main__':
    dataset, target = InitializeData()
    predictions = []
    epochErrors = []

    lr = 0.001
    epochNum = 350

    model = Model()

    epochErrors = model.TrainNetwork(dataset, target, lr, epochNum)
    for sample in dataset:
        predictions.append(np.asarray(model.PredictValues(sample)).item())

    DrawPlots(epochNum, epochErrors, dataset, target, predictions)
