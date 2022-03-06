import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def CreateHeatmap(columns):
    data = pd.read_csv("csvFiles/corrMat.csv")

    plt.figure(figsize=(26,18), dpi= 80)
    sns.heatmap(data, cmap="mako", xticklabels = columns[0:-1], yticklabels = columns[0:-1], annot = True)

    plt.title('Heatmap', fontsize=42)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.show()

def CreateHistogram(list):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    feature = pd.read_csv('csvFiles/dataset.csv')
    gTotal = feature[str(list[0][-2])].dropna()
    kgf = feature[str(list[0][-1])].dropna()
    sns.histplot(gTotal, bins=4, kde=False, ax=axes[0], color="green")
    sns.histplot(kgf, bins=10, kde=False, ax=axes[1], color="purple")
    plt.show()
    #print(df.info())
