def solution(n, results):
    answer = 0
    board = [[0] * n for _ in range(n)]
    
    for win, lose in results:
        board[win-1][lose-1] = 1
        board[lose-1][win-1] = -1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][k] == 1 and board[k][j] == 1:
                    board[i][j] = 1
                elif board[i][k] == -1 and board[k][j] == -1:
                    board[i][j] = -1
    for i in range(n):
        if board[i].count(0) == 1:
            answer += 1           
    return answer


