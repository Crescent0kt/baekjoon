#초기화
import sys

N = int(sys.stdin.readline())
board = [0]*N
#확인하기
def check(board,row,col):
    #모든 행에 대해서 순차적으로 탐색
    for i in range(row):
        #1. 같은 열인가
        #2. 대각선에 위치하나
        if board[i] == col:
            return False
        elif board[i] + (row-i) == col or board[i] - (row-i) ==col:
            return False
    else:
        return True

def dfs(row):
    #종료 조건 row >= N
    if row>=N:
        return 1
    answer = 0
    for col in range(N):
        if check(board,row,col):
            board[row] = col
            answer += dfs(row+1)
    return answer

a = dfs(0)
print(a)

