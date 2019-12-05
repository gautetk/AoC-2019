import os

chalange = 'Day2-1'
sourcePath = '..\\Source\\'
source = sourcePath + 'Day2-1' + '.txt'
resultPath = '..\\Result\\'
result = resultPath + chalange + '.txt'

sourceFile = open(source, 'r')
inputCode = sourceFile.read()

splitedInputCode = inputCode.split(',')
memory = map(int, splitedInputCode)

memory[1]=12
memory[2]=2

memory[1]=0
memory[2]=1

keepOn = True
possition = 0
while keepOn == True:
    if memory[possition] == 1:
        memory[memory[possition + 3]] = memory[memory[possition + 1]] + memory[memory[possition + 2]]
    elif memory[possition] == 2:
        memory[memory[possition + 3]] = memory[memory[possition + 1]] * memory[memory[possition + 2]]
    elif memory[possition] == 99:
        keepOn = False
    possition = possition +4
        

output = memory[0]
print output
print memory

resultFile = open(result, 'w+')
resultFile.write(str(output))

sourceFile.close
resultFile.close
