import sys
import heapq

INF = sys.maxsize

N,M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append([v,w])
    graph[v].append([u,w])

x, z = map(int,sys.stdin.readline().split())
P = int(sys.stdin.readline())
mid = [int(x) for x in sys.stdin.readline().split()]

def dijkstra(start):
    dist = [INF] * (N+1)
    pq = []
    dist[start] = 0
    heapq.heappush(pq,[0, start])
    
    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if dist[cur_node] < cur_cost: continue
        
        for next_node, next_cost in graph[cur_node]:
            cost = next_cost+cur_cost
            if cost<dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(pq,[cost,next_node])
    return dist

distx = dijkstra(x)
distz = dijkstra(z)

result = INF
for y in mid:
    ans = distx[y] + distz[y]
    if ans < result:
        result = ans

if result >= INF : print(-1)
else : print(result)