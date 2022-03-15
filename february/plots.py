import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def CreateHeatmap(columns):
    data = pd.read_csv("csvFiles/corrMat.csv")

    fig = plt.figure(figsize=(26,18), dpi= 80)
    sns.heatmap(data, cmap="mako", xticklabels = columns[0:-1], yticklabels = columns[0:-1], annot = True)

    plt.title('Heatmap', fontsize=42)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.show()
    fig.savefig('plots/heatmap.png', dpi=150)

def CreateDistribution(features, list):
    feature = pd.read_csv('csvFiles/dataset.csv')
    for j in range(2, len(list[0])):
        fig = plt.figure(figsize=(12, 12), dpi=80)
        name = feature[str(list[0][j])].dropna()
        sns.displot(name, kind="kde")
        #sns.histplot(name, bins=8, color="green")
        plt.axvline(x=float(features[5][j - 1]), color='blue', linestyle='dashed', linewidth=2)
        plt.axvline(x=float(features[6][j - 1]), color='purple', linestyle='dashed', linewidth=2)
        plt.axvline(x=float(features[7][j - 1]), color='pink', linestyle='dashed', linewidth=2)
        plt.tight_layout()
        plt.show()
        #fig.savefig('plots/' + str(j) + 'Column.png', dpi=150)

def CreateHistogram(gainRatio, list):
    plt.barh(list[0][:-2], gainRatio)
    plt.tight_layout()
    plt.figure(figsize=(36, 18), dpi=80)
    plt.show()

