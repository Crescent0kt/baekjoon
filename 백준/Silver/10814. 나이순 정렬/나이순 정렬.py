import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for i in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)

    heapq.heappush(heap,(age,i,name))

for _ in range(N):
    age, _, name = heapq.heappop(heap)
    print(age, name)
