import sys
import heapq
from collections import defaultdict
INF = int(1e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a][b] = min(c,graph[a][b])

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j] if graph[i][j] != INF else 0,end = " ")
    print("")
