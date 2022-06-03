import choose_room as choose
import graph
import analyze

testResult = choose.test()
winningRate_changed_test = testResult[0]
winningRate_kept_test = testResult[1]
numberOfRooms = testResult[2]

mathematicalResult = choose.mathmatic(numberOfRooms)
winningRate_changed_math = mathematicalResult[0]
winningRate_kept_math = mathematicalResult[1]

errorRate_changed = analyze.errorrange(winningRate_changed_test, winningRate_changed_math, numberOfRooms)
errorRate_kept = analyze.errorrange(winningRate_kept_test, winningRate_kept_math, numberOfRooms)
betterOne = analyze.whichisbetter(winningRate_changed_test, winningRate_kept_test, numberOfRooms)
changedIsBetter = betterOne[0] #integer
keptIsBetter = betterOne[1] #list
same = betterOne[2] # list

print("\n")
print(":::::::::::::::Setting:::::::::::::::\n")
print(f"Max number of rooms : {numberOfRooms}")
print(f"number of iteration : {testResult[3]}")
print()

print(":::::::::::::::Result:::::::::::::::\n")
print("Winning rate when you change your choice")
print(f"tested : {winningRate_changed_test}")
print(f"calculated : {winningRate_changed_math}\n")

print("Winning rate when you kept your choice")
print(f"tested : {winningRate_kept_test}")
print(f"calculated : {winningRate_kept_math}\n")

print(f"If you change your choice, the error rate is below {errorRate_changed}")
print(f"If you keep your choice, the error rate is below {errorRate_kept}\n")
print(f"The number of times it was advantageous to change your choice : {changedIsBetter}")
if len(keptIsBetter) >= 1:
    print(f"The number of times it was advantageous to keep your choice : {len(keptIsBetter)}")
    print(f"  It is when the number of room is : {keptIsBetter}")
    if len(keptIsBetter) == 1:
        print(f"  The winning rate is {winningRate_kept_test[keptIsBetter[0] - 3]}")
    else:
        print(f"  The winning rate is between {winningRate_kept_test[keptIsBetter[0] - 3]} and {winningRate_kept_test[keptIsBetter[-1] - 3]}")

    wrongResult = False
    for n in keptIsBetter:
        if winningRate_kept_math[n - 3] < winningRate_changed_math[n - 3]:
            wrongResult = True
        else:
            wrongResult = False
    if wrongResult == True:
        print ("  The result Is mathematically wrong. It is always more advantageous when you change your choice.")
if len(same) >= 1:
    print(f"the number of time two of them was same : {len(same)}")
    print(f"  It is when the number of room is : {same}")
    if len(same) == 1:
        print(f"  The winning rate is {winningRate_changed_test[same[0] - 3]}")
    else:
        print(f"  The winning rate is between {winningRate_changed_test[same[0] - 3]} and {winningRate_changed_test[same[-1] - 3]}")
    wrongResult = False
    for n in same:
        if winningRate_kept_math[n - 3] < winningRate_changed_math[n - 3]:
            wrongResult = True
        else:
            wrongResult = False
    if wrongResult == True:
        print("  The result Is mathematically wrong. It is always more advantageous when you change your choice.")

graph.drawGraph(winningRate_changed_test, winningRate_kept_test, winningRate_changed_math, winningRate_kept_math, numberOfRooms)
