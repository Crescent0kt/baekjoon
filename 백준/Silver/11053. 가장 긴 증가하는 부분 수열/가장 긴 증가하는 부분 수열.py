import sys

N = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))

D = [1] * N

for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            D[i] = max(D[i],D[j]+1)

print(max(D))