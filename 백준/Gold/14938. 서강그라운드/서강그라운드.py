import sys
import heapq
from collections import defaultdict
INF = int(1e9)
n,m,r = map(int,sys.stdin.readline().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

items = list(map(int,sys.stdin.readline().split()))

for _ in range(r):
    a,b,l = map(int,sys.stdin.readline().split())
    graph[a][b] = l
    graph[b][a] = l

for i in range(1,n+1):
    graph[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+ graph[k][j])


maximum_items = 0
for i in range(1,n+1):
    item_i = 0
    for j in range(1,n+1):
        if graph[i][j] <= m:
            item_i += items[j-1]
    maximum_items = max(maximum_items, item_i)

print(maximum_items)