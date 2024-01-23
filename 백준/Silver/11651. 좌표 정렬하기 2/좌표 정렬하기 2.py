import sys
import heapq

heap = []

N = int(sys.stdin.readline())

for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    heapq.heappush(heap,(y,x))

for _ in range(N):
    y,x = heapq.heappop(heap)
    print(x, y)
    