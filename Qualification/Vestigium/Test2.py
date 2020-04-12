import numpy as np
f = open("Test1.txt", "r")

def input():
    return f.readline()
def Vestigum(arr, size):
    nArray = np.asarray(arr)
    # Diag Count
    diagCount = np.trace(nArray)
    # Row Count
    rowCount = 0
    # Column Count
    colCount = 0
    for i in range(size):
        if (not allUnique(nArray[i,:])):
            rowCount += 1
        if (not allUnique(nArray[:,i])):
            colCount += 1
    return '%s %s %s' % (diagCount, rowCount,colCount)

def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

for case in range(int(input())):
    arrLen = input()
    arr = []
    for i in range(int(arrLen)):
        row = input().strip().split()
        arr.append(list(map(lambda x: int(x), row)))
    print('Case #%d: %s' % (case+1, Vestigum(arr, int(arrLen))))