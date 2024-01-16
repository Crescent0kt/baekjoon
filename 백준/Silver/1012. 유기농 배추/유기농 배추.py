"""
입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50),
그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.
"""
dx = [-1,0,1,0]
dy = [0, -1 ,0,1]
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    M,N,K = map(int,sys.stdin.readline().split())
    ans =0
    cabbage = [([0] * M) for _ in range(N)]
    for _ in range(K):
        x,y = map(int,sys.stdin.readline().split())
        cabbage[y][x] = 1

    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 0:
                continue

            stack = [(i,j)]
            cabbage[i][j] = 0
            
            while stack:
                y,x = stack.pop()
                for k in range(4):
                    cx = dx[k] + x
                    cy = dy[k] + y
                    if 0<=cx<M and 0<=cy<N and cabbage[cy][cx] == 1:
                        stack.append((cy,cx))
                        cabbage[cy][cx] = 0
            ans += 1
    print(ans)
        
                