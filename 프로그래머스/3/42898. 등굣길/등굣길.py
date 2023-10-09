def solution(m, n, puddles):
    answer = 0
    
    board = list(([0] * m) for _ in range(n))
    for x,y in puddles:
        board[y-1][x-1] = -1
    
    board[0][0] = 1
    
    for i in range(1,m):
        if board[0][i] != -1:
            board[0][i] = board[0][i-1]

    for i in range(1,n):
         if board[i][0] != -1:
            board[i][0] = board[i-1][0]
            
            
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j] != -1:
                if board[i][j-1] != -1:
                    board[i][j] += board[i][j-1]
                if board[i-1][j] != -1:
                    board[i][j] += board[i-1][j]
            
    return board[n-1][m-1]%1000000007