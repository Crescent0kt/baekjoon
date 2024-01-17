import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    arr.append(list(sys.stdin.readline().rstrip()))

ans = []
dx = [0,-1,0,1]
dy = [-1,0,1,0]

for i in range(N):
    for j in range(N):
        if arr[i][j] == "0":
            continue
        count = 1
        stack = [(i,j)]
        arr[i][j] = "0" 
        while stack:
            y,x = stack.pop()
            
            for k in range(4):
                cx = x + dx[k]
                cy = y + dy[k]

                if 0<=cx and cx<N and 0<=cy and cy < N and arr[cy][cx] == "1":
                    arr[cy][cx] = "0" 
                    stack.append((cy,cx))
                    count += 1
        ans.append(count)

print(len(ans))
ans.sort()
for a in ans:
    print(a)