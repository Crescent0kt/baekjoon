import sys
import heapq
INF = int(1e9)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

m,n = map(int,sys.stdin.readline().split())
board = []

for _ in range(n):
    board.append([int(c) for c in sys.stdin.readline().rstrip()])

visited = [[INF]*m for _ in range(n)]
visited[0][0] = 0
q = []
q.append((0,0,0))
ans = 0
while q:
    x,y,count = heapq.heappop(q)

    if visited[y][x] <count:
        continue

    if y==n-1 and x ==m-1:
        ans = count
        break

    count += board[y][x]

    for i in range(4):
        cx = dx[i]+x
        cy = dy[i]+y
        if 0<=cx<m and 0<=cy<n and visited[cy][cx] > count:
            visited[cy][cx] = count
            heapq.heappush(q,(cx,cy,count))
print(ans)