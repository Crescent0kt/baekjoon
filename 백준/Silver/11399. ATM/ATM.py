import sys
import heapq

N = int(sys.stdin.readline())
q=  list(map(int,sys.stdin.readline().split()))
heapq.heapify(q)

ans = 0
aa = 0
for i in range(N):
    aa = aa + heapq.heappop(q)
    ans = ans + aa

print(ans)

    