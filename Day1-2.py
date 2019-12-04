import os

chalange = 'Day1-2'
sourcePath = '..\\Source\\'
source = sourcePath + 'Day1-1' + '.txt'
resultPath = '..\\Result\\'
result = resultPath + chalange + '.txt'

sourceFile = open(source, 'r')
sourceFileLines = sourceFile.readlines()

fuel = 0
for mass in sourceFileLines:
    positiveFuel = True
    tmpMass = mass
    while positiveFuel == True:
        tmpFuel = int(float(tmpMass)/3)-2
        if tmpFuel > 0:
            fuel = fuel + tmpFuel
            tmpMass = tmpFuel
        else:
            positiveFuel = False


print fuel

resultFile=open(result, 'w+')
resultFile.write(str(fuel))

sourceFile.close
resultFile.close
