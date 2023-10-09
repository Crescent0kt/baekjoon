import sys
from itertools import combinations

N,M = map(int,sys.stdin.readline().split())

board = [] * N
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

tmp = combinations(range(M),3)

ans = 0
for a,b,c in tmp:
    count = 0
    for i in range(N):
        count += max(board[i][a],board[i][b],board[i][c])
    if ans< count:
        ans = count

print(ans)