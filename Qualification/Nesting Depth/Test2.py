f = open("Test1.txt", "r")

def input():
    return f.readline()

def NestingDepth(splitArr):
    outputStr = ''
    for i in range(len(splitArr)):
        outputStr += str(int(splitArr[i]) * '(') + splitArr[i] + str(int(splitArr[i]) * ')')
    while ')(' in outputStr:
        outputStr = outputStr.replace(')(', '')
    return '%s' % (outputStr)

for case in range(int(input())):
    arr = []
    split = list(input().strip())
    print('Case #%d: %s' % (case+1, NestingDepth(split)))