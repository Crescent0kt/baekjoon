import sys
import heapq
from collections import defaultdict
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    arr = [0] * (N+1)
    arr[0] = 1
    arr[1] = 1
    for i in range(2,N+1):
        arr[i] = arr[i-1]+arr[i-2]
    print(arr[N])