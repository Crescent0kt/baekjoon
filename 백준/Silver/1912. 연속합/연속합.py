import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

D = [0] * n
D[0] = arr[0]
for i in range(1,n):
    if arr[i] > D[i-1]+arr[i]:
        D[i] = arr[i]
    else:  D[i] =  D[i-1]+arr[i]

print(max(D))