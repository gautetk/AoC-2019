import os
from operator import itemgetter


def main():
    chalange = 'Day8-2'
    sourcePath = '..\\Source\\'
    source = sourcePath + 'Day8' + '.txt'
    resultPath = '..\\Result\\'
    result = resultPath + chalange + '.txt'

    wide = 25
    tall = 6

    sourceFile = open(source, 'r')
    sourceFileLine = sourceFile.readline()

    layers = getLayers(sourceFileLine, wide, tall)

    image = getMessage(layers, wide, tall)

    print image

    imagePrint = [image[x:x+25] for x in range(0, len(image), 25)]
    print imagePrint

    for line in imagePrint:
			print ' '.join(line)


def getMessage(layers, wide, tall):
    image = []
    for x in range(wide*tall):
        for layer in layers:
            if layer[x] == 0:
                image.append(' ')
                break
            elif layer[x] == 1:
                image.append('#')
                break

    return image


def getLayers(line, wide, tall):
    intList = []
    layers = []
    for value in line:
        value = int(value)
        intList.append(value)
    pixelCount = wide * tall
    layers = [intList[x:x+pixelCount]
              for x in range(0, len(intList), pixelCount)]
    return layers


if __name__ == "__main__":
    main()
