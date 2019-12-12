import os


def main():
    chalange = 'Day7'
    sourcePath = '..\\Source\\'
    source = sourcePath + chalange + '.txt'

    with open(source, 'r') as sourceFile:
        inputCode = sourceFile.read()

    splitedInputCode = inputCode.split(',')
    initialMemory = map(int, splitedInputCode)


    part1(initialMemory)


def part1(initialMemory):
    initialSettings = [0, 1, 2, 3, 4]

    maxSignal = 0
    for a in initialSettings:
        for b in filter(lambda b: b not in [a], initialSettings):
            for c in filter(lambda c: c not in [a, b], initialSettings):
                for d in filter(lambda d: d not in [a, b, c], initialSettings):
                    for e in filter(lambda e: e not in [a, b, c, d], initialSettings):
                        aSettings = [a, b, c, d, e]
                        signal = 0
                        for setting in aSettings:
                            memory = initialMemory[:]
                            signal = runCode(memory, [setting, signal])
                        if signal > maxSignal:
                            maxSignal = signal
    print maxSignal


def runCode(memory, inputValues):
    ip = 0
    i = 0
    count = 0
    output = []
    while count < 100000000:
        count += 1
        istruction = memory[ip]
        if istruction % 100 == 1:
            memory[memory[ip + 3]] = getValue(memory, istruction,ip, 1) + getValue(memory, istruction, ip, 2)
            ip += 4
        elif istruction % 100 == 2:
            memory[memory[ip + 3]] = getValue(memory, istruction,ip, 1) * getValue(memory, istruction, ip, 2)
            ip += 4
        elif istruction % 100 == 3:
            memory[memory[ip + 1]] = inputValues[i]
            i = i+1
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
    return output[0]


def getValue(memory, instruction, ip, valuePos):
    mode = (instruction/(10*10**valuePos)) % 10
    if mode == 0:
        value = memory[memory[ip+valuePos]]
    else:
        value = memory[ip+valuePos]
    return value


if __name__ == "__main__":
    main()
