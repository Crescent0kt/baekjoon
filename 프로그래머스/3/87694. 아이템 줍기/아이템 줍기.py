from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    board = [[0] * 102 for _ in range(102)]
    cx = [0,-1,0,1]
    cy = [1,0,-1,0]
    
    for x1,y1,x2,y2 in rectangle:
        for i in range(y1*2,y2*2+1):
            for j in range(x1*2,x2*2+1):
                if y1*2 == i or y2*2 == i or x1*2 == j or x2*2 == j:
                    board[i][j] = max(1,board[i][j])
                else:
                    board[i][j] = 2
    q = deque()
    q.append((characterX * 2, characterY *2, 1))
    
    while q:
        x,y,c = q.popleft()
        if x == itemX *2 and itemY *2 == y:
            return c//2
        board[y][x] = 0
        for i in range(4):
            dx = x + cx[i]
            dy = y + cy[i]
            if 0<=dx<=101 and 0<=dy<=101 and board[dy][dx] == 1:
                q.append((dx,dy,c+1))
        
    
    return answer