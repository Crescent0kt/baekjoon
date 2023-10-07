import sys
import heapq

INF = sys.maxsize
N,M = map(int,sys.stdin.readline().split())
E = list([] for _ in range(N+1))
for _ in range(M):
    u,v,w = map(int,sys.stdin.readline().split())
    E[u].append([v,w])
x,y,z = map(int,sys.stdin.readline().split())

def Dijkstra(start,active):
    dist = [INF] * (N+1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq,[0,start])

    if active:
        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            if dist[cur_node] < cur_cost: continue
            for next_node, next_cost in E[cur_node]:
                if dist[next_node] > cur_cost+next_cost:
                    dist[next_node] = cur_cost+next_cost
                    heapq.heappush(pq, [cur_cost+next_cost, next_node])

    else:
        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            if dist[cur_node] < cur_cost: continue
            for next_node, next_cost in E[cur_node]:
                if next_node == y: continue
                if dist[next_node] > cur_cost+next_cost:
                    dist[next_node] = cur_cost+next_cost
                    heapq.heappush(pq, [cur_cost+next_cost, next_node])
    return dist


dist1 = Dijkstra(x,True)
dist2 = Dijkstra(y,True)
dist3 = Dijkstra(x, False)

ans1 = dist1[y]+dist2[z]
ans2 = dist3[z]

if ans1>=INF : ans1 = -1
if ans2>=INF : ans2 = -1
print(ans1,ans2)