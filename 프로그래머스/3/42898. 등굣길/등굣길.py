def solution(m, n, puddles):
    answer = 0

    board = [[0] * (m) for _ in range(n)]
    
    for x,y in puddles:
        board[y-1][x-1] = -1
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == -1:
                board[i][j] = 0
                continue
                
            if i == 0 and j == 0:
                board[i][j] = 1
                continue
            
            if i == 0:
                board[i][j] = board[i][j-1]
            
            elif j == 0:
                board[i][j] = board[i-1][j]
                
            else:
                board[i][j] = board[i-1][j] + board[i][j-1]
            
    return board[n-1][m-1]%1000000007