import os

chalange = 'Day1-1'
sourcePath = '..\\Source\\'
source = sourcePath + chalange + '.txt'
resultPath = '..\\Result\\'
result = resultPath + chalange + '.txt'

sourceFile = open(source, 'r')
sourceFileLines = sourceFile.readlines()

fuel = 0
for mass in sourceFileLines:
    tmpFuel = int(float(mass)/3)-2
    fuel = fuel + tmpFuel

print fuel

resultFile=open(result, 'w+')
resultFile.write(str(fuel))

sourceFile.close
resultFile.close
