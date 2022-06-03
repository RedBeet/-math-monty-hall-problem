import random
repeat = int(input("Input how many times you will repeat : "))

def choosing_room():
    myFirstChoice = random.randint(1, 3)
    winRoom = random.randint(1, 3)
    openedRoom = random.randint(1, 3)
    myFinalChoice = random.randint(1, 3)

    while openedRoom == myFirstChoice:
        openedRoom = random.randint(1, 3)
    while myFinalChoice == myFirstChoice or myFinalChoice == openedRoom:
        myFinalChoice = random.randint(1, 3)

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
        print(f"testing...{n}/{repeat}")
    changeWinRate = (changeWinCount / repeat) * 100
    keepWinRate = (keepWinCount / repeat) * 100

    return changeWinCount,keepWinCount, changeWinRate, keepWinRate

result = montyhall()
print(f"{repeat}times repeated")
print(f"Number of wins(change) : {result[0]}")
print(f"Number of wins(keep) : {result[1]}")
print(f"Winning rate(change) : {result[2]}")
print(f"Winning rate(keep) : {result[3]}")