import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

conn = {}
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    if a not in conn:
        conn[a] = [b]
    else:
        conn[a].append(b)
    if b not in conn:
        conn[b] = [a]
    else:
        conn[b].append(a)
stack = []
visited = [0] * (N+1)

stack.append(1)
visited[1] = 1

while stack:
    num = stack.pop()
    if num in conn:
        for con in conn[num]:
            if visited[con] ==0:
                visited[con] += 1
                stack.append(con)

print(sum(visited)-1)