import os


def main():
    chalange = 'Day3-1'
    sourcePath = '..\\Source\\'
    source = sourcePath + 'Day3' + '.txt'
    resultPath = '..\\Result\\'
    result = resultPath + chalange + '.txt'

    sourceFile = open(source, 'r')
    sourceFileLines = sourceFile.readlines()

    jumps1 = splitInput(sourceFileLines[0])
    jumps2 = splitInput(sourceFileLines[1])

    possitions1 = getPath(jumps1)
    possitions2 = getPath(jumps2)

    crossings = getCrossings(possitions1, possitions2)

    closestCrossing = getClosestCrossing(crossings)

    print closestCrossing


def getClosestCrossing(crossings):
    minDistance = 9999999999999
    for crossing in crossings:
        distance = abs(crossing[0]) + abs(crossing[1])
        if distance < minDistance:
            minDistance = distance
    return minDistance


def splitInput(line):
    splitedInputCode = line.split(',')
    jumps = map(lambda x: [x[0], int(x[1:])], splitedInputCode)
    return jumps


def getPath(jumps):
    possitions = [[0, 0]]
    for jump in jumps:
        for increment in range(0, jump[1]):
            possitions.append(getIncrement(possitions[-1], jump[0]))
    return possitions[1:]


def getIncrement(possition, direction):
    if direction == 'R':
        newPossition = [possition[0] + 1, possition[1]]
    elif direction == 'L':
        newPossition = [possition[0] - 1, possition[1]]
    elif direction == 'U':
        newPossition = [possition[0], possition[1] + 1]
    elif direction == 'D':
        newPossition = [possition[0], possition[1] - 1]
    return newPossition


def getCrossings(possitions1, possitions2):
    crossings = []
    for pos1 in possitions1:
        for pos2 in possitions2:
            if pos1 == pos2:
                crossings.append(pos1)
    return crossings


if __name__ == "__main__":
    main()
