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


keepOn = True
instructionPointer = 0
count = 0
while keepOn == True and count < 1000000:
    if memory[instructionPointer] == 1:
        memory[memory[instructionPointer + 3]] = memory[memory[instructionPointer + 1]] + memory[memory[instructionPointer + 2]]
    elif memory[instructionPointer] == 2:
        memory[memory[instructionPointer + 3]] = memory[memory[instructionPointer + 1]] * memory[memory[instructionPointer + 2]]
    elif memory[instructionPointer] == 99:
        keepOn = False
    instructionPointer = instructionPointer +4
    count = count + 1
        

output = memory[0]
print output
print memory

resultFile = open(result, 'w+')
resultFile.write(str(output))

sourceFile.close
resultFile.close
