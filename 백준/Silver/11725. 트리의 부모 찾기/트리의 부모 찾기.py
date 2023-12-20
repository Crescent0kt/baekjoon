import sys
from collections import defaultdict
N = int(sys.stdin.readline())
# 0 - 7
visited = [0] * (N+1)
d = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    d[a].append(b)
    d[b].append(a)

stack = [1]
while stack:
    node = stack.pop()
    next_nodes = d[node]
    for next_node in next_nodes:
        if visited[next_node] == 0:
            visited[next_node] = node
            stack.append(next_node)

for visit in visited[2:]:
    print(visit)