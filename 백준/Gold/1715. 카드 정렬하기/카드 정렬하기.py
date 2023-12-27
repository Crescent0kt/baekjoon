import sys
import heapq

n = int(sys.stdin.readline())

cards = []
count = 0
for _ in range(n):
    heapq.heappush(cards,int(sys.stdin.readline()))

while len(cards)>1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    c = a+b
    count += c
    heapq.heappush(cards,c)

print(count)
