import sys
from collections import defaultdict
from collections import deque
N, M, V = map(int,sys.stdin.readline().split())

dict = defaultdict(list)

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    dict[a].append(b)
    dict[b].append(a)

#1 DFS
visited = [False] * (N+1)

stack = deque([V])

while stack:
    node = stack.popleft()
    if visited[node] != True:
        visited[node] = True
        print(node, end=" ")
        dict[node].sort(reverse=True)
        for next_node in dict[node]:
            if visited[next_node] != True:
                stack.appendleft(next_node)


print("")
#2 BFS
visited = [False] * (N+1)

stack = deque([V])

while stack:
    node = stack.popleft()
    if visited[node] != True:
        visited[node] = True
        print(node, end=" ")
        dict[node].sort()
        for next_node in dict[node]:
            if visited[next_node] != True:
                stack.append(next_node)

