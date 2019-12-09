import os
from operator import itemgetter


def main():
    chalange = 'Day8-1'
    sourcePath = '..\\Source\\'
    source = sourcePath + 'Day8' + '.txt'
    resultPath = '..\\Result\\'
    result = resultPath + chalange + '.txt'

    wide = 25
    tall = 6

    sourceFile = open(source, 'r')
    sourceFileLine = sourceFile.readline()

    layers, zeroes = getLayers(sourceFileLine, wide, tall)

    idx, number = getNumber(zeroes, layers)

    # print val
    print idx
    print number

def getNumber(zeroes, layers):
    idx = min(enumerate(zeroes), key=itemgetter(1))[0]
    number1 = 0
    number2 = 0
    for row in layers[idx]:
        for value in row:
            if value == 1:
                number1 = number1+1
            elif value == 2:
                number2 = number2+1
    number = number1*number2
    return idx, number


def getLayers(line, wide, tall):
    layers = []
    layer = []
    row = []
    numberOfZeros = 0
    zeros = []
    for i, value in enumerate(line):
        value = int(value)
        row.append(value)
        if value == 0:
            numberOfZeros = numberOfZeros + 1
        if i % (wide*tall) == (wide*tall)-1:
            layer.append(row)
            layers.append(layer)
            zeros.append(numberOfZeros)
            row = []
            layer = []
            numberOfZeros = 0
        elif i % wide == wide-1:
            layer.append(row)
            row = []
    return layers, zeros


if __name__ == "__main__":
    main()
