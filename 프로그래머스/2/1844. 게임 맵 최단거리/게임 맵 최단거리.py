from collections import deque
import sys
y = [0,-1,0,1]
x = [-1,0,1,0]
inf = sys.maxsize

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = list([inf] * m for _ in range(n))
    
    dq = deque()
    dq.append((0,0))
    visited[0][0] = 1
    
    while len(dq) != 0:
        
        uy,ux = dq.popleft()
        
        for i in range(4):
            dx = ux+x[i]
            dy = uy+y[i]
            if 0<=dx<m and 0<=dy<n and maps[dy][dx] != 0:
                if visited[dy][dx] > visited[uy][ux] +1:
                    visited[dy][dx] = visited[uy][ux] +1
                    dq.append((dy,dx))
    answer = visited[n-1][m-1]
    if answer == inf: answer = -1 
    return answer