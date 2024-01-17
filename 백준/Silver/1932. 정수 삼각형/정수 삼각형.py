import sys

N = int(sys.stdin.readline())

arr = [0] * N

for i in range(N):
    tmpArr = arr[:]
    numList = list(map(int,sys.stdin.readline().split()))

    arr[0] += numList[0]
    for j in range(1,len(numList)):
        arr[j] = max(tmpArr[j-1], tmpArr[j]) + numList[j]


print(max(arr))