import sys
import heapq

INF = sys.maxsize
N,E = map(int,sys.stdin.readline().split())

graph = list([] for _ in range(N+1))
for _ in range(E):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

v1,v2 = map(int,sys.stdin.readline().split())

def Dijkstra(start):
    dist = [INF] * (N+1)
    pq = []
    heapq.heappush(pq,[0,start])
    dist[start] = 0

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if dist[cur_node] < cur_cost: continue
        for next_node, next_cost in graph[cur_node]:
            cost = cur_cost+next_cost
            if cost<dist[next_node]:
                heapq.heappush(pq,[cost,next_node])
                dist[next_node] = cost
    return dist
distx = Dijkstra(1)
distv1 = Dijkstra(v1)
distv2 = Dijkstra(v2)

ans1= distx[v1]+distv1[v2]+distv2[N]
ans2 = distx[v2]+distv2[v1]+distv1[N]

if ans1 >= INF and ans2>=INF : print(-1)
elif ans1>ans2:print(ans2)
else :print(ans1)

