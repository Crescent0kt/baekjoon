import sys

N = int(sys.stdin.readline())
arr1 = [x for x in range(N,0,-1)]
arr2 = []
arr3 = []
count = 0
while count < N:
    #명령어 받는 줄
    C, D = map(int, sys.stdin.readline().split())
    if C == 1:
        for i in range(D):
            arr2.append(arr1.pop())
    else:
        for i in range(D):
            arr3.append(arr2.pop())
            count += 1
arr3.reverse()
for a in arr3:
    print(a)