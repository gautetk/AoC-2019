import os


def main():
    chalange = 'Day7'
    sourcePath = '..\\Source\\'
    source = sourcePath + chalange + '.txt'

    with open(source, 'r') as sourceFile:
        inputCode = sourceFile.read()

    splitedInputCode = inputCode.split(',')
    initialMemory = map(int, splitedInputCode)

    part2(initialMemory)


def part2(initialMemory):
    initialSettings = [5, 6, 7, 8, 9]

    maxSignal = 0
    for a in initialSettings:
        for b in filter(lambda b: b not in [a], initialSettings):
            for c in filter(lambda c: c not in [a, b], initialSettings):
                for d in filter(lambda d: d not in [a, b, c], initialSettings):
                    for e in filter(lambda e: e not in [a, b, c, d], initialSettings):
                        aSettings = [a, b, c, d, e]
                        maxSignal = getSignal(aSettings, initialMemory, maxSignal)
    print maxSignal


def getSignal(aSettings, initialMemory, maxSignal):

    ip = [0]*5
    outputs = [None]*5
    signal = [0]
    inputs = map(lambda x: [x], aSettings)
    inputPos = [0]*5
    memory = [initialMemory[:]]*5
    finished = [False]*5
    while finished[4] != True:
        for i, setting in enumerate(aSettings):
            inputs[i].extend(signal)
            ip[i], memory[i], outputs[i], inputPos[i], finished[i] = runCode(ip[i], memory[i], inputs[i], inputPos[i])
            signal = outputs[i]
    if signal > maxSignal:
        maxSignal = signal
    return maxSignal


def runCode(ip, memory, inputValues, inputPos):
    count = 0
    finished = False
    output = []
    while count < 100000000:
        count += 1
        istruction = memory[ip]
        if istruction % 100 == 1:
            memory[memory[ip + 3]] = getValue(memory, istruction, ip, 1) + getValue(memory, istruction, ip, 2)
            ip += 4
        elif istruction % 100 == 2:
            memory[memory[ip + 3]] = getValue(memory, istruction, ip, 1) * getValue(memory, istruction, ip, 2)
            ip += 4
        elif istruction % 100 == 3:
            if len(inputValues) < inputPos+1:
                return ip, memory, output, inputPos, finished
            else:
                memory[memory[ip + 1]] = inputValues[inputPos]
                inputPos += 1
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
            finished = True
            return ip, memory, output, inputPos, finished
    # return output[0], memory[:]


def getValue(memory, instruction, ip, valuePos):
    mode = (instruction/(10*10**valuePos)) % 10
    if mode == 0:
        value = memory[memory[ip+valuePos]]
    else:
        value = memory[ip+valuePos]
    return value


if __name__ == "__main__":
    main()
