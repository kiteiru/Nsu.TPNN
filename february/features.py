import csv
from math import nan, sqrt

def CountDeviation(average, amount, list):
    sum = 0
    for i in range(len(list)):
        sum += pow(list[i] - average, 2)
    return sqrt(sum/amount)

def FeaturesMatrix(list):
    names = ['Amount', 'NaN %', 'Min', 'Max', '1st quartile', 'Median', '3rd quartile', 'Average value', 'Standart deviation', 'Cardinality', 'Interquartile range']
    features = []
    rowSize = len(list[0])
    colSize = len(list)

    features.append([''])

    for j in range(2, rowSize):
        features[0].append(list[0][j])
        if j < len(names) + 2:
            features.append([names[j-2]])

    for j in range(2, rowSize):
        amount = 0
        sum = 0
        min = 1e6
        max = 0
        unique = []
        sorted = []
        for i in range(1, colSize):
            elem = float(list[i][j])
            if elem is not nan:
                sum += elem
                amount += 1
                if elem < min:
                    min = elem
                if elem > max:
                    max = elem
                if elem not in unique:
                    unique.append(elem)
                sorted.append(elem)

        nanAmount = 100 * (1 - (amount / (colSize - 1)))

        sorted.sort()
        first = 0.25 * (amount + 1)
        second = 0.5 * (amount + 1)
        third = 0.75 * (amount + 1)

        if first - int(first) != 0:
            num = int(first) - 1
            firstQuartile = (sorted[num] + sorted[num + 1]) / 2
        else:
            firstQuartile = sorted[int(first)]
        if second - int(second) != 0:
            num = int(second) - 1
            median = (sorted[num] + sorted[num + 1]) / 2
        else:
            median = sorted[int(second)]
        if third - int(third) != 0:
            num = int(third) - 1
            thirdQuartile = (sorted[num] + sorted[num + 1]) / 2
        else:
            thirdQuartile = sorted[int(third)]

        average = sum / amount
        deviation = CountDeviation(average, amount, sorted)
        cardinality = len(unique)
        interquartileRange = thirdQuartile - firstQuartile

        features[1].append(str(amount))
        features[2].append(str(round(nanAmount, 2)))
        features[3].append(str(min))
        features[4].append(str(max))
        features[5].append(str(round(firstQuartile, 2)))
        features[6].append(str(round(median, 2)))
        features[7].append(str(round(thirdQuartile, 2)))
        features[8].append(str(round(average, 2)))
        features[9].append(str(round(deviation, 2)))
        features[10].append(str(cardinality))
        features[11].append(str(round(interquartileRange, 2)))

    #print(features)

    with open("csvFiles/featMat.csv", "w+") as file:
        fileWriter = csv.writer(file)
        for i in range(len(features)):
            fileWriter.writerow(features[i])