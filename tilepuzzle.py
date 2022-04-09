## tilepuzzle.py
## I set the depth limit 32. If you want, you can change it on line 132.

import copy

## the interface function
def tilepuzzle(start,goal):
    depth = 0
    return reverse(statesearch([start],goal,[], depth))

def statesearch(unexplored,goal,path, depth):
    if unexplored == []:
        return []
    elif goal == head(unexplored):
        return cons(goal,path)
    else:
        # generate new states and find visited states
        newStates = generateNewStates(head(unexplored), depth)
        visitedStates = []
        for i in range(len(newStates)):
            if newStates[i] in path:
                visitedStates.append(newStates[i])

        # remove visited states from new states generated above
        for i in range(len(visitedStates)):
            newStates.remove(visitedStates[i])

        depth += 1 # go one level down

        result = statesearch(newStates,
                             goal,
                             cons(head(unexplored), path), depth)
        if result != []:
            return result
        else:
            # check the remainning states if the first one fails
            return statesearch(tail(unexplored),
                               goal,
                               path, depth)

## A function that finds the space(0)'s position in the tile.
def searchSpacePostion(list):
    result = []
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == 0:
                # store a pair of number in the list
                result.append(i)
                result.append(j)
                return result

## A function that checks if the next move can be executed.
def checkIfSpaceCanMove(rowIndex, colIndex):

    # valid index must be in the range of 0 to 2
    if rowIndex < 0 or rowIndex > 2 or colIndex < 0 or colIndex > 2:
        return False
    else:
        return True

## A function that moves space left if possible.
def generateMoveSpaceLeft(currState):

    #find the position of empty tile
    spacePos = searchSpacePostion(currState)
    oldRowIndex, oldColIndex = spacePos[0], spacePos[1]

    # reduce the column index by one
    newRowIndex, newColIndex = oldRowIndex, oldColIndex - 1

    if checkIfSpaceCanMove(newRowIndex, newColIndex) == True:
        # move space left by swapping values in the tile
        currState[oldRowIndex][oldColIndex] = currState[newRowIndex][newColIndex]
        currState[newRowIndex][newColIndex] = 0
        return currState
    else:
        return []

## A function that moves space right if possible.
def generateMoveSpaceRight(currState):
    spacePos = searchSpacePostion(currState)
    oldRowIndex, oldColIndex = spacePos[0], spacePos[1]

    # increase the column index by one
    newRowIndex, newColIndex = oldRowIndex, oldColIndex + 1

    if checkIfSpaceCanMove(newRowIndex, newColIndex) == True:
        # move space right by swapping values in the tile
        currState[oldRowIndex][oldColIndex] = currState[newRowIndex][newColIndex]
        currState[newRowIndex][newColIndex] = 0
        return currState
    else:
        return []

## A function that moves space up if possible.
def generateMoveSpaceUp(currState):
    spacePos = searchSpacePostion(currState)
    oldRowIndex, oldColIndex = spacePos[0], spacePos[1]

    # reduce the row index by one
    newRowIndex, newColIndex = oldRowIndex - 1, oldColIndex

    if checkIfSpaceCanMove(newRowIndex, newColIndex) == True:
        # move space left by swapping values in the tile
        currState[oldRowIndex][oldColIndex] = currState[newRowIndex][newColIndex]
        currState[newRowIndex][newColIndex] = 0
        return currState
    else:
        return []

## A function that moves space down if possible.
def generateMoveSpaceDown(currState):
    spacePos = searchSpacePostion(currState)
    oldRowIndex, oldColIndex = spacePos[0], spacePos[1]

    # increase the row index by one
    newRowIndex, newColIndex = oldRowIndex + 1, oldColIndex

    if checkIfSpaceCanMove(newRowIndex, newColIndex) == True:
        # move space left by swapping values in the tile
        currState[oldRowIndex][oldColIndex] = currState[newRowIndex][newColIndex]
        currState[newRowIndex][newColIndex] = 0
        return currState
    else:
        return []

## A function that gennerate all new states and stores them in a list
def generateNewStates(currState, depth):
    result = []

    # return empty list if the depth beyonds the limit 32
    if depth > 32:
        return result

    # deep copy four lists without changging the current state
    copyCurrStateLeft = copy.deepcopy(currState)
    copyCurrStateRight = copy.deepcopy(currState)
    copyCurrStateUp = copy.deepcopy(currState)
    copyCurrStateDown = copy.deepcopy(currState)

    # gennerate next possible moves
    moveSpaceLeftRes = generateMoveSpaceLeft(copyCurrStateLeft)
    moveSpaceRightRes = generateMoveSpaceRight(copyCurrStateRight)
    moveSpaceUpRes = generateMoveSpaceUp(copyCurrStateUp)
    moveSpaceDownRes = generateMoveSpaceDown(copyCurrStateDown)

    # store them if they are not empty
    if moveSpaceLeftRes != []:
        result.append(moveSpaceLeftRes)

    if  moveSpaceRightRes != []:
        result.append(moveSpaceRightRes)

    if  moveSpaceUpRes != []:
        result.append(moveSpaceUpRes)

    if moveSpaceDownRes != []:
        result.append(moveSpaceDownRes)

    return result

## some utility functions from pegpuzzle.py
def reverse(st):
    return st[::-1]
    
def head(lst):
    return lst[0]

def tail(lst):
    return lst[1:]

def cons(item,lst):
    return [item] + lst