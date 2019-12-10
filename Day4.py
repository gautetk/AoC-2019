import os
from operator import itemgetter


def main():
    chalange = 'Day8'

    inputRangeMin = 235741
    inputRangeMax = 706948

    part2(inputRangeMin, inputRangeMax)

def part2(inputRangeMin, inputRangeMax):
    valid = []
    for i in range(inputRangeMin, inputRangeMax):
        number = map(int, str(i))
        decreasing = checkDecreasing(number)
        if decreasing==False:
            double= checkDoublePart2(number)
            if double==True:
                valid.append(number)
    print valid
    print len(valid)


def part1(inputRangeMin, inputRangeMax):
    valid = []
    for i in range(inputRangeMin, inputRangeMax):
        number = map(int, str(i))
        decreasing = checkDecreasing(number)
        if decreasing==False:
            double= checkDouble(number)
            if double==True:
                valid.append(number)
    print len(valid)
            
def checkDoublePart2(number):
    double=False
    number.append(-1)
    number.insert(0, -1)
    for i in range(len(number)-2):
        if number[i+1] == number[i+2]:
            if number[i+1] != number[i+3] and number[i+1] != number[i]:
                double=True
                break
    return double

def checkDouble(number):
    double=False
    j=-1
    for i in number:
        if i == j:
            double=True
        else:
            j=i
    return double
        
def checkDecreasing(number):
    j=0
    decreasing=False
    for i in number:
        if i>=j:
            j=i
        else:
            decreasing=True
            break
    return decreasing




if __name__ == "__main__":
    main()
