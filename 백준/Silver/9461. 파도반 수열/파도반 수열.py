import sys

T = int(sys.stdin.readline())

D = [0] *(101)

D[1] = D[2] = 1

for i in range(3,101):
    D[i] = D[i-2] + D[i-3]

for _ in range(T):
    print(D[int(sys.stdin.readline())])