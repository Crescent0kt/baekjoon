from collections import deque

M,N = map(int,input().split())

dx = [0, -1 ,0 ,1]
dy = [-1, 0 ,1 ,0]

board = []
tomato = 0

Q = deque()

for i in range(N):
    row = list(map(int,input().split()))
    board.append(row)
    for j in range(M):
        if row[j] == -1:
            continue

        if row[j] == 1:
            Q.append((i,j))
        tomato += 1

count = 0
days = 1

while len(Q) != 0:
    x, y = Q.popleft()
    count += 1
    if days < board[x][y]:
        days = board[x][y]

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if 0<= nx < N and 0<= ny < M and board[nx][ny] == 0:
            #큐에넣고, 보드값 현재 + 1로 변경
            Q.append((nx,ny))
            board[nx][ny] = board[x][y]+1

if tomato <= count:
    print(days-1)
else: print(-1)