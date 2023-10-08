import sys

n = int(sys.stdin.readline())

D = [0] * (n+1)

#D[0]은 비울거기때문에 D배열 접근시 +1
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    tmp = D[:]
    for i, num in enumerate(arr):
        D[i+1] = max(tmp[i],tmp[i+1]) + num

print(max(D))