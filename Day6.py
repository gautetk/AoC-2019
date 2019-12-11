import os
from operator import itemgetter


def main():
    chalange = 'Day6'
    sourcePath = '..\\Source\\'
    source = sourcePath + chalange + '.txt'

    sourceFile = open(source, 'r')
    sourceFileLines = sourceFile.readlines()

    lines = map(lambda x: x.rstrip('\n'), sourceFileLines)
    lines = map(lambda x: x.split(')'), lines)
    orbitObject = {}
    for line in lines:
        orbitObject[line[1]] = line[0]

    part2(orbitObject)


def part1(orbitObject):
    cnt = 0
    for key in list(orbitObject.keys()):
        tmp = key
        while tmp in orbitObject:
            cnt = cnt + 1
            tmp = orbitObject[tmp]
    print cnt


def part2(orbitObject):

    you = {}
    cnt = 0
    tmp = orbitObject['YOU']
    while tmp in orbitObject:
        you[tmp] = cnt
        cnt = cnt+1
        tmp = orbitObject[tmp]

    san = {}
    cnt = 0
    tmp = orbitObject['SAN']
    while tmp in orbitObject:
        san[tmp] = cnt
        cnt = cnt+1
        tmp = orbitObject[tmp]

    jumps = []
    for key in you:
        if key in san:
            jump = san[key]+you[key]
            jumps.append(jump)
    print min(jumps)


if __name__ == "__main__":
    main()
