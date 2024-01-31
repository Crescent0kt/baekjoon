import sys
from collections import defaultdict

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

arr = defaultdict(list)

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

stack = [1]
visited = [False] * (N+1)
visited[1] = True
count = 0
while stack:
    node = stack.pop()

    for next_node in arr[node]:
        if visited[next_node] == False:
            visited[next_node] = True
            stack.append(next_node)
            count += 1
print(count)