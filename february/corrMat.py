import csv
from math import nan, sqrt

def CountCorrMat(list):
    corrMat = []
    rowSize = len(list[0])
    colSize = len(list)

    corrMat.append([])
    for j in range(2, rowSize):
        corrMat[0].append(list[0][j])

    for i in range(2, rowSize):
        corrMat.append([])
        for j in range(2, rowSize):
            sumX = 0
            squareSumX = 0
            sizeX = 0
            sumY = 0
            squareSumY = 0
            sizeY = 0
            sumXY = 0
            for k in range(1, colSize):
                xi = float(list[k][i])
                yi = float(list[k][j])

                if xi is not nan and yi is not nan:
                    sumX += xi
                    sumY += yi
                    sizeX += 1
                    sizeY += 1

            meanX = sumX / sizeX
            meanY = sumY / sizeY
            for k in range(1, colSize):
                xi = float(list[k][i])
                yi = float(list[k][j])

                if xi is not nan and yi is not nan:
                    sumXY += ((xi - meanX) * (yi - meanY))
                    squareSumX += ((xi - meanX) * (xi - meanX))
                    squareSumY += ((yi - meanY) * (yi - meanY))

            divider = sqrt(squareSumX * squareSumY)
            if divider != 0:
                corr = sumXY / divider
                corrMat[i-1].append(round(abs(corr), 3))
            else:
                corrMat[i-1].append('')

    #print(corrMat)

    with open("csvFiles/corrMat.csv", "w+") as file:
        fileWriter = csv.writer(file)
        for i in range(len(corrMat)):
            fileWriter.writerow(corrMat[i])
