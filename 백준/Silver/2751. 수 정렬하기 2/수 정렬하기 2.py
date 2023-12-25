import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    heapq.heappush(heap,num)

for _ in range(N):
    num = heapq.heappop(heap)
    print(num)
