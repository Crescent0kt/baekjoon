def solution(maps):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    inf = int(10e9)

    N = len(maps)
    M = len(maps[0])
    board = [[inf] * M for _ in range(N)]
    arr = [(0,0,1)]
    while arr:
        x,y,n = arr.pop(0)
        if board[y][x] <= n:
            continue
        board[y][x] = n
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if M> cx >=0 and N>cy >=0  and maps[cy][cx] != 0:
                if board[cy][cx] > n+1:
                    arr.append((cx,cy,n+1))

    if board[N-1][M-1] == inf:
        return -1
    else:
        return board[N-1][M-1]
    