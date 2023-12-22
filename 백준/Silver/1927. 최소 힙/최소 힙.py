import heapq
import sys
N = int(sys.stdin.readline())

min_heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if not min_heap:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap,x)