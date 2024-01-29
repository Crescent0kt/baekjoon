import sys

arr = [0] * 100
for i in range(100):
    if i == 1 or i == 2 or i == 0:
        arr[i] = 1
    else:
        arr[i] = arr[i-3] + arr[i-2]
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    print(arr[N-1])