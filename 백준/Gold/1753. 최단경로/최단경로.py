
import sys
import heapq
INF = sys.maxsize
V,E = map(int,sys.stdin.readline().split())
#시작정점
K = int(sys.stdin.readline())
graph = list([] for _ in range(V+1))
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append([v,w])

pq = []
heapq.heappush(pq,[0,K])
dist = [INF] * (V+1)
dist[K] = 0

while pq:
    cur_cost, cur_node = heapq.heappop(pq)
    
    if cur_cost > dist[cur_node]: continue
    for next_node, next_cost in graph[cur_node]:
        if next_cost + cur_cost < dist[next_node]:
            dist[next_node] = next_cost + cur_cost
            heapq.heappush(pq,[next_cost + cur_cost,next_node])

for i in range(1,len(dist)):
    if dist[i] >= INF: print("INF")
    else: print(dist[i])