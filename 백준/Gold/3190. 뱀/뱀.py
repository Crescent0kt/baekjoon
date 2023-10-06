from collections import deque
#문제 초기화
N = int(input())
K = int(input())

#보드 생성
board = list([0]* (N+2) for _ in range(N+2))

#사과두기
for _ in range(K):
    y, x = map(int,input().split())
    board[y][x] = 1

for i in range(N+2):
    board[0][i] = -1
    board[N+1][i] = -1
    board[i][0] = -1
    board[i][N+1] = -1

#방향 전환 정보
direction = deque()

L = int(input())
for i in range(L):
    sec, way = input().split()
    direction.append((int(sec),way))

#뱀정보
snake = deque()
head = (1,1)
# 상 우 하 좌
dx = [0, 1, 0 ,-1]
dy = [-1 ,0 ,1 ,0]

#상 우 하 좌 : 0 1 2 3 시작은 오른쪽
direct = 1
count = 0
sec,way = direction.popleft()

while True:
    #시간부터 올리고
    count += 1
    #뱀 머리 이동
    hy, hx = head
    nx = hx + dx[direct]
    ny = hy + dy[direct]
    head = (ny,nx)
    #벽이거나 뱀에 닿으면 죽음
    if board[ny][nx] == -1:
        break

    #사과면 기존 헤드 자리에 추가
    elif board[ny][nx] == 1:
        snake.append((hy,hx))
        board[hy][hx] = -1
        board[ny][nx] = 0
    #빈공간이면 전진(헤드 전 위치를 스택 마지막으로 대체)
    else:
        #헤드의 전 위치를 끝에 넣고, 보드 바꿈
        snake.append((hy,hx))
        board[hy][hx] = -1
        #헤드의 꼬리를 빼고 보드를 빈공간으로 만듬
        ty, tx = snake.popleft()
        board[ty][tx] = 0

    #시간에 맞춰서 방향전환
    if sec == count:
        if way == "L":
            direct = (direct + 3) % 4
        else:
            direct = (direct +1) % 4
        if len(direction) != 0:
            sec,way = direction.popleft()
print(count)