import csv
from math import nan
from features import FeaturesMatrix
from corrMat import CountCorrMat
from classes import SeparateOnClasses
from plots import CreateHistogram, CreateHeatmap

def FillEmptyCells():
    for i in range(listSize):
        rowSize = len(list[i])
        for j in range(rowSize - 1):
            if list[i][j] == "-" or list[i][j] == "" or list[i][j] == "не спускался":
                list[i][j] = nan
            if list[i][j] is not nan:
                if "," in list[i][j]:
                    list[i][j] = list[i][j].replace(",", ".")
        JoinKGF(list, rowSize, i)
        list[i].pop()
#
def JoinKGF(list, rowSize, i):
    if list[i][rowSize - 1] != "-" and list[i][rowSize - 1] != "" and i > 2:
        list[i][rowSize - 1] = list[i][rowSize - 1].replace(",", ".")
        list[i][rowSize - 2] = float(list[i][rowSize - 1]) * 1000

list = []
with open ("csvFiles/ID_data_mass_18122012.csv", "r") as file:
    idx = 0
    fileReader = csv.reader(file)
    for row in fileReader:
        if idx < 3:
            list.append(row)
            idx += 1
            continue
        last = len(row) - 1
        if (row[last] != "-" and row[last] != "") or (row[last - 1] != "-" and row[last - 1] != ""):
            list.append(row)
        idx += 1

listSize = len(list)

FillEmptyCells()

rowSize = len(list[0])
for i in range(rowSize):
    if type(list[0][i]) == str:
        list[1][i] = str(list[1][i]) + ": " + str(list[0][i]) + " "
    list[1][i] = str(list[1][i]) + " [" + str(list[2][i]) + "]"

del list[2]
del list[0]

columns = []
for j in range(2, rowSize):
    columns.append(list[0][j])

CountCorrMat(list)
CreateHeatmap(columns)
FeaturesMatrix(list)
SeparateOnClasses(list)
#CreateHistogram(list)

with open ("csvFiles/dataset.csv", "w+") as file:
    fileWriter = csv.writer(file)
    for i in range(len(list)):
        fileWriter.writerow(list[i])

