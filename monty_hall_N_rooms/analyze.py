from math import fabs

def errorrange(test, math, numberOfRooms):
    error = []
    for i in range(numberOfRooms - 2):
        error.append(fabs(test[i] - math[i]))
    maxError = round(max(error), 3)

    return maxError

def whichisbetter(changed, kept, numberOfRooms):
    changedIsBetter = 0
    keptIsBetter = []
    same = []
    for i in range(numberOfRooms - 2):
        if changed[i] > kept[i]:
            changedIsBetter += 1
        elif kept[i] > changed[i]:
            keptIsBetter.append(i + 3)
        else:
            same.append(i + 3)

    return changedIsBetter, keptIsBetter, same
