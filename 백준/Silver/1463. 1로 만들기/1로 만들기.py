import sys

N = int(sys.stdin.readline())
INF = sys.maxsize
D = [INF] *(N+1)

D[N] = 0

for i in range(N,0,-1):
    if i%3 == 0:
        D[i//3] = min(D[i]+ 1, D[i//3])

    if i%2 ==0:
        D[i//2] = min(D[i]+ 1, D[i//2])

    D[i-1] = min(D[i]+1, D[i-1])

print(D[1])