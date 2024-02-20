import sys

blue = 0
white = 0

N = int(sys.stdin.readline())
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

stack = [(0, 0, N)]


def func(w, h, N):
    is_white = False
    global blue
    global white
    if board[h][w] == 0:
        is_white = True
    for i in range(N):
        next = 0
        for j in range(N):
            if is_white and board[h + i][w + j] == 1:
                func(w, h, N // 2)
                func(w, h+ (N // 2), N // 2)
                func(w+ (N // 2), h, N // 2)
                func(w + (N // 2), h + (N // 2), N // 2)
                break
            elif not is_white and board[h + i][w + j] == 0:
                func(w, h, N // 2)
                func(w, h+ (N // 2), N // 2)
                func(w+ (N // 2), h, N // 2)
                func(w + (N // 2), h + (N // 2), N // 2)
                break
        else:
            next = 1
        if next != 1:
            break
    else:
        if is_white:
            white += 1
        else:
            blue += 1

func(0,0,N)
print(white)
print(blue)
