import sys

N = int(sys.stdin.readline())

apart = []
count = 0
num_apart = []
dx = [-1,0,1,0]
dy = [0,-1,0,1]


# 아파트 상태 확인
for _ in range(N):
    apart.append(list(sys.stdin.readline().rstrip()))



for i in range(N):
    for j in range(N):
        if apart[i][j] == "0": continue
        else:
            count += 1
            num = 1
            #x,y 순서
            stack = [(i, j)]
            apart[i][j] = "0"
            while stack:
                cy, cx = stack.pop()
                for k in range(4):
                    y = cy + dy[k]
                    x = cx + dx[k]
                    if 0 <= x  and x < N and 0 <= y and y < N :
                        if apart[y][x] != "0":
                            num +=1
                            stack.append((y,x))
                            apart[y][x] = "0"
            num_apart.append(num)
print(count)
num_apart.sort()
for i in num_apart:
    print(i)
