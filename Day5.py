import os


def main():
    chalange = 'Day5'
    sourcePath = '..\\Source\\'
    source = sourcePath + 'Day5' + '.txt'

    with open(source, 'r') as sourceFile:
        inputCode = sourceFile.read()

    splitedInputCode = inputCode.split(',')
    initialMemory = map(int, splitedInputCode)

    inputValue = 1 #Part1
    inputValue = 5 #Part2

    output = runCode(initialMemory, inputValue)
    print output


def runCode(memory, inputValue):
    ip = 0
    count = 0
    output = []
    while count < 100000000:
        count += 1
        istruction = memory[ip]
        if istruction % 100 == 1:
            memory[memory[ip + 3]] = getValue(memory, istruction,
                                              ip, 1) + getValue(memory, istruction, ip, 2)
            ip += 4
        elif istruction % 100 == 2:
            memory[memory[ip + 3]] = getValue(memory, istruction,
                                              ip, 1) * getValue(memory, istruction, ip, 2)
            ip += 4
        elif istruction % 100 == 3:
            memory[memory[ip + 1]] = inputValue
            ip += 2
        elif istruction % 100 == 4:
            value = getValue(memory, istruction, ip, 1)
            output.append(value)
            ip += 2
        elif istruction % 100 == 5:
            if getValue(memory, istruction, ip, 1) != 0:
                ip = getValue(memory, istruction, ip, 2)
            else:
                ip += 3
        elif istruction % 100 == 6:
            if getValue(memory, istruction, ip, 1) == 0:
                ip = getValue(memory, istruction, ip, 2)
            else:
                ip += 3
        elif istruction % 100 == 7:
            if getValue(memory, istruction, ip, 1) < getValue(memory, istruction, ip, 2):
                memory[memory[ip + 3]] = 1
            else:
                memory[memory[ip + 3]] = 0
            ip += 4
        elif istruction % 100 == 8:
            if getValue(memory, istruction, ip, 1) == getValue(memory, istruction, ip, 2):
                memory[memory[ip + 3]] = 1
            else:
                memory[memory[ip + 3]] = 0
            ip += 4
        elif istruction % 100 == 99:
            break
    return output


def getValue(memory, instruction, ip, valuePos):
    mode = (instruction/(10*10**valuePos)) % 10
    if mode == 0:
        value = memory[memory[ip+valuePos]]
    else:
        value = memory[ip+valuePos]
    return value


if __name__ == "__main__":
    main()