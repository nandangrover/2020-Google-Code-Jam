f = open("Test1.txt", "r")

def input():
    return f.readline()

def Expogo(splitArr):
    outputString = ''
    inputSum = sum(splitArr)
    stepList = calculateSteps(abs(inputSum))
    if (splitArr[0] == 0 and splitArr[1] == 0):
        return 'IMPOSSIBLE'
    if len(stepList):
        for i in range(len(stepList)):
            x = splitArr[0]
            y = splitArr[1]
            if (abs(splitArr[0]) > abs(splitArr[1])):
                if (x < 0):
                    splitArr[0] = splitArr[0] + stepList[0]
                    outputString += 'W'
                else:
                    splitArr[0] = splitArr[0] - stepList[0]
                    outputString += 'E'
                stepList.pop(0)
            elif (abs(splitArr[0]) < abs(splitArr[1])):
                if (y < 0):
                    splitArr[1] = splitArr[1] + stepList[0]
                    outputString += 'S'
                else:
                    splitArr[1] = splitArr[1] - stepList[0]
                    outputString += 'N'
                stepList.pop(0)
    if (splitArr[0] == 0 and splitArr[1] == 0 and len(stepList) == 0):
        return outputString[::-1]
    return 'IMPOSSIBLE'

def calculateSteps(inputSum):
    stepArr = []
    i = 1
    while sum(stepArr) < inputSum:
        stepArr.append(2**(i-1))
        i += 1
    stepArr.sort(reverse=True)
    return stepArr
for case in range(int(input())):
    row = input().strip().split()
    print('Case #%d: %s' % (case+1, Expogo(list(map(lambda x: int(x), row)))))