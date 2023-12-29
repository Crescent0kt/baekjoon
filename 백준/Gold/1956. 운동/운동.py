import sys
import heapq
from collections import defaultdict
INF = int(1e9)
V,E = map(int,sys.stdin.readline().split())

graph = [[INF] * (V+1) for _ in range(V+1)]

ans = INF
for _ in range(E):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a][b] = c


for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
            if i == j:
                ans = min(ans, graph[i][i])

if ans == INF:
    print(-1)
else:
    print(ans)