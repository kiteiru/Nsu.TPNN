import copy
import csv
from math import nan, log


def CountInfoXAndSplitX(list, T, existingClasses, infoX, splitInfoX):
    uniqueElems = {}
    infoForInfoX =[]
    lastExisting = copy.deepcopy(existingClasses)

    # for j in range(len(list[0])):
    for j in range(0, 1):
        whetherInClass = {}
        # for i in range(1, len(list)):
        for i in range(1, len(list)):
            idx = list[i][j]
            if idx not in uniqueElems:
                uniqueElems[idx] = 1
            else:
                uniqueElems[idx] += 1

            if idx not in whetherInClass:
                whetherInClass[idx] = {}
                for key in lastExisting:
                    if i in lastExisting[key]:
                        if key not in whetherInClass[idx]:
                            whetherInClass[idx][key] = 1
                        else:
                            whetherInClass[idx][key] += 1
                        lastExisting[key].remove(i)
                        break
            else:
                for key in lastExisting:
                    if i in lastExisting[key]:
                        if key not in whetherInClass[idx]:
                            whetherInClass[idx][key] = 1
                        else:
                            whetherInClass[idx][key] += 1
                        lastExisting[key].remove(i)
                        break
        info = 0
        infoPerClass = []
        sum = 0
        for key in whetherInClass:
            for key2 in whetherInClass[key]:
                sum += (whetherInClass[key][key2] / uniqueElems[key])
            infoPerClass.append(sum * -1)
        information = 0
        iter = 0
        for key in uniqueElems:
            division = uniqueElems[key] / T
            information += division * infoPerClass[iter]
            iter += 1
        infoX.append(round(information, 3))

        print("\ninfoX")
        print(infoX)

        print("\nunique elems")
        print(uniqueElems)
        split = 0
        for key in uniqueElems:
            division = uniqueElems[key] / T
            split += division * log(division, 2)
        split *= -1
        splitInfoX.append(round(split, 3))
        print("\nsplitX")
        print(splitInfoX)

        '''for key in whetherInClass:
            for k in range(len(whetherInClass[key])):'''

    print("\n\nexist")
    print(existingClasses)

    print("\n\nwhether")
    print(whetherInClass)



def CountInfo(existingClasses, T):
    sum = 0
    for key in existingClasses:
        freq = len(existingClasses[key])
        freqDivideT = freq / T
        sum += (freqDivideT * log(freqDivideT, 2))
    return -1 * sum


def CountGainRatio(existingClasses, T, list):
    gainRatio = 0
    info = CountInfo(existingClasses, T)
    infoX = []
    splitInfoX = []
    CountInfoXAndSplitX(list, T, existingClasses, infoX, splitInfoX)


    return gainRatio


def SeparateOnClasses(list):
    target = []
    gTotal = []
    kgf = []
    column = len(list[0]) - 2

    target.append([])
    target[0].append(list[0][column])
    target[0].append(list[0][column + 1])

    for i in range(1, len(list)):
        target.append([])
        target[i].append(list[i][column])
        target[i].append(list[i][column + 1])
        if list[i][column] is not nan:
            gTotal.append(float(list[i][column]))
        if list[i][column + 1] is not nan:
            kgf.append(float(list[i][column + 1]))

    gTotal.sort()
    kgf.sort()
    # gTotal.append(nan)

    gTotalIntervals = []
    kgfIntervals = []
    gTotalAmountPerInterval = []
    kgfAmountPerInterval = []

    gTotalIntervalsNum = 6
    kgfIntervalsNum = 8

    floor = len(gTotal) // gTotalIntervalsNum

    residue = len(gTotal) % gTotalIntervalsNum
    for i in range(gTotalIntervalsNum):
        if residue != 0:
            gTotalAmountPerInterval.append(floor + 1)
            residue -= 1
        else:
            gTotalAmountPerInterval.append(floor)

    floor = len(kgf) // kgfIntervalsNum
    residue = len(kgf) % kgfIntervalsNum
    for i in range(kgfIntervalsNum):
        if residue != 0:
            kgfAmountPerInterval.append(floor + 1)
            residue -= 1
        else:
            kgfAmountPerInterval.append(floor)

    left = 0
    for i in range(len(gTotalAmountPerInterval)):
        gTotalIntervals.append([])
        right = left + gTotalAmountPerInterval[i]

        gTotalIntervals[i].append(gTotal[left])
        gTotalIntervals[i].append(gTotal[right - 1])

        left += gTotalAmountPerInterval[i]

    gTotalIntervals.append([nan])
    gTotalAmountPerInterval.append(1)
    gTotalIntervalsNum += 1

    left = 0
    for i in range(len(kgfAmountPerInterval)):
        kgfIntervals.append([])
        right = left + kgfAmountPerInterval[i]

        kgfIntervals[i].append(kgf[left])
        kgfIntervals[i].append(kgf[right - 1])

        left += kgfAmountPerInterval[i]

    classes = []

    for i in range(gTotalIntervalsNum):
        for j in range(kgfIntervalsNum):
            classes.append([])
            classes[i * (gTotalIntervalsNum + 1) + j].append(gTotalIntervals[i])
            classes[i * (gTotalIntervalsNum + 1) + j].append(kgfIntervals[j])

    existingClasses = {}
    for i in range(1, len(target)):
        if target[i][0] is nan:
            firstIdx = len(gTotalIntervals) - 1
        else:
            for j in range(len(gTotalIntervals)):
                if gTotalIntervals[j][0] <= float(target[i][0]) <= gTotalIntervals[j][1]:
                    firstIdx = j

        for j in range(len(kgfIntervals)):
            if kgfIntervals[j][0] <= float(target[i][1]) <= kgfIntervals[j][1]:
                secondIdx = j

        classNum = firstIdx * (gTotalIntervalsNum + 1) + secondIdx

        if classNum not in existingClasses:
            existingClasses[classNum] = []
            existingClasses[classNum].append(i)
        else:
            examples = existingClasses[classNum]
            examples.append(i)
            existingClasses[classNum] = examples

    '''print("gtotal: ")
    print(gTotalIntervals)
    print("kgf: ")
    print(kgfIntervals)
    print("\n\nclasses: ")
    print(existingClasses)'''

    T = len(target) - 1
    gainRatio = CountGainRatio(existingClasses, T, list)

    with open("csvFiles/target.csv", "w+") as file:
        fileWriter = csv.writer(file)
        for i in range(len(target)):
            fileWriter.writerow(target[i])
