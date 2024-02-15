import sys

N = int(sys.stdin.readline())
arr = [[0] * 3 for i in range(N)]

for i in range(N):
    r, g, b = map(int,sys.stdin.readline().split())
    if i == 0:
        arr[i][0] = r
        arr[i][1] = g
        arr[i][2] = b

    else:
        arr[i][0] = min(arr[i - 1][1], arr[i - 1][2]) + r
        arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + g
        arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + b

print(min(arr[-1]))