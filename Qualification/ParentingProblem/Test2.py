
f = open("Test1.txt", "r")

def input():
    return f.readline()

def ParentingProblemSolve(arr, size):
    outputString = ''
    cameron = ''
    jamie = ''
    for i in range(size):
        subStr = ''
        for j in range(arr[i][0], arr[i][1]+1):
            subStr += ',' + str(j) + ','
        lowLimit = (arr[i][0])
        upLimit = (arr[i][1])
        if((int(lowLimit) > 1440 or int(upLimit) > 1440) or int(lowLimit) > int(upLimit)):
             outputString = 'IMPOSSIBLE'
             break
        if (checkIfNumberNotInRanges(lowLimit,upLimit, cameron)):
            outputString += 'J'
            cameron += subStr
        elif (checkIfNumberNotInRanges(lowLimit,upLimit, jamie)):
            outputString += 'C'
            jamie += subStr
        else:
            outputString = 'IMPOSSIBLE'
            break
    return '%s' % (outputString)

def checkIfNumberNotInRanges(low, up, string):
    for i in range(low+1,up):
            if (',' + str(i) + ',' in string):
                return False
    return True

for case in range(int(input())):
    arrLen = input()
    arr = []
    for i in range(int(arrLen)):
        row = input().strip().split()
        arr.append(list(map(lambda x: int(x), row)))
    print('Case #%d: %s' % (case+1, ParentingProblemSolve(arr, int(arrLen))))