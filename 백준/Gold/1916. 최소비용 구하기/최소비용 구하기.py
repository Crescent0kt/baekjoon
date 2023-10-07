import sys
import heapq

INF = sys.maxsize
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = list([] for _ in range(N+1))

for _ in range(M):
    x,y,c = map(int,sys.stdin.readline().split())
    #도착/비용 순서
    graph[x].append([y,c])

#출발점에서 도착점의 도시 번호를 줌

start, end = map(int,sys.stdin.readline().split())

pq = []
heapq.heappush(pq,[0, start])
dist = [INF] * (N+1)
dist[start] = 0

while pq:
    cur_cost, cur_node = heapq.heappop(pq)
    if dist[cur_node] <cur_cost : continue
    for next_node, next_cost in graph[cur_node]:
        cost=cur_cost+next_cost
        if cost < dist[next_node]:
            dist[next_node] = cost
            heapq.heappush(pq,[cost, next_node])


print(dist[end])