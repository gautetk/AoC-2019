import os


def main():
    chalange = 'Day5'
    sourcePath = '..\\Source\\'
    source = sourcePath + 'Day5' + '.txt'

    sourceFile = open(source, 'r')
    inputCode = sourceFile.read()

    splitedInputCode = inputCode.split(',')
    initialMemory = map(int, splitedInputCode)

#     target=19690720
    
#     noun, verb = calculateMemoryWithTarget(initialMemory, target)
            
#     output = str(noun)+str(verb)
#     print output

#     resultFile = open(result, 'w+')
#     resultFile.write(str(output))

#     sourceFile.close
#     resultFile.close

# def calculateMemoryWithTarget(initialMemory, target):
#     for noun in range(0,100):
#         for verb in range(0,100):
#             memory=initialMemory[:]
#             memory[1]=noun
#             memory[2]=verb
#             tmpOutput=runCode(memory)
#             if tmpOutput == target:
#                 return noun, verb

# def runCode(memory):
#     keepOn = True
#     instructionPointer = 0
#     count = 0
#     while keepOn == True and count < 1000000000:
#         if memory[instructionPointer] == 1:
#             memory[memory[instructionPointer + 3]] = memory[memory[instructionPointer + 1]] + memory[memory[instructionPointer + 2]]
#         elif memory[instructionPointer] == 2:
#             memory[memory[instructionPointer + 3]] = memory[memory[instructionPointer + 1]] * memory[memory[instructionPointer + 2]]
#         elif memory[instructionPointer] == 99:
#             keepOn = False
#         instructionPointer = instructionPointer + 4
#         count = count + 1
#     return memory[0]

if __name__ == "__main__":
    main()