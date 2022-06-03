import random


def test():
    print("Monty hall problem with N rooms!")
    maxNumberOfRooms = int(input("Input the maximum number of rooms : "))
    repeat = int(input("Input how many times you will repeat in each experiment : "))
    winningRate_changed = []
    winningRate_kept = []

    def choosing_room():
        myFirstChoice = random.randint(1, i)
        winRoom = random.randint(1, i)
        openedRoom = random.randint(1, i)
        myFinalChoice = random.randint(1, i)

        while openedRoom == myFirstChoice or openedRoom == winRoom:
            openedRoom = random.randint(1, i)
        while myFinalChoice == myFirstChoice or myFinalChoice == openedRoom:
            myFinalChoice = random.randint(1, i)

        return myFinalChoice, winRoom, myFirstChoice

    def montyhall():
        changeWinCount = 0
        keepWinCount = 0
        
        for n in range(repeat):
            room = choosing_room()
            changedChoice = room[0]
            winningRoom = room[1]
            keptChoice = room[2]
            if changedChoice == winningRoom:
                changeWinCount += 1
            elif keptChoice == winningRoom:
                keepWinCount += 1
            print(f"testing {i} rooms...{n}/{repeat}")
        changeWinRate = (changeWinCount / repeat) * 100
        keepWinRate = (keepWinCount / repeat) * 100

        return changeWinRate, keepWinRate

    for i in range(3, maxNumberOfRooms + 1):
        result = montyhall()
        winningRate_changed.append(result[0])
        winningRate_kept.append(result[1])

    return winningRate_changed, winningRate_kept, maxNumberOfRooms, repeat


def mathmatic(maxNoOfRooms):
    winningRate_changed = []
    winningRate_kept = []

    def montyhall_change():
        winRate = ((currentNumberOfRooms - 1) / (currentNumberOfRooms ** 2 - 2 * currentNumberOfRooms)) * 100

        return winRate

    def montyhall_keep():
        winRate = (1 / currentNumberOfRooms) * 100
        return winRate

    for currentNumberOfRooms in range(3, maxNoOfRooms + 1):
        winningRate_changed.append(montyhall_change())
        winningRate_kept.append(montyhall_keep())
        print(f"calculating {currentNumberOfRooms} rooms...")

    return winningRate_changed, winningRate_kept