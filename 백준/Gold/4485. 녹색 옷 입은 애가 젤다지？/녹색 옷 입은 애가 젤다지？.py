import sys
import heapq


dx = [-1,0,1,0]
dy = [0,-1,0,1]
INF = int(1e9)
aaaaa=  0
while True:
    aaaaa +=1 
    graph = []
    N = int(sys.stdin.readline())
    if N == 0:
        break
    for _ in range(N):
        graph.append(list(map(int,sys.stdin.readline().split())))

    visited = [[INF] * N for _ in range(N)]

    ans = 0
    visited[0][0] = graph[0][0]

    q= [(graph[0][0],0,0)]
    while q:
        cost, x,y = heapq.heappop(q)
        if visited[y][x] < cost:
            continue

        ans += graph[y][x]
        if x == N-1 and y == N-1:
            print("Problem %s: %s" %(aaaaa,visited[y][x]))
            break

        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y

            if 0<=cx<N and 0<=cy<N and visited[cy][cx] > cost + graph[cy][cx]:
                new_cost = cost + graph[cy][cx]
                visited[cy][cx] = new_cost
                heapq.heappush(q,(new_cost,cx,cy))