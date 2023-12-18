import sys
import collections

def dfs(stack, visited):
    answer = []
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        answer.append(node)

        if node in graph_dict:
            edges = graph_dict[node]
        else:
            continue
        edges.sort(reverse=True)
        for edge in edges:
            if not visited[edge]:
                stack.append(edge)
    print(*answer)
def bfs(queue, visited):
    answer = []
    while queue:
        node = queue.popleft()
        if visited[node]:
            continue
        visited[node] = True
        answer.append(node)
        if node in graph_dict:
            edges = graph_dict[node]
        else:
            continue
        edges.sort()
        for edge in edges:
            if not visited[edge]:
                queue.append(edge)
    print(*answer)



N,M,V = map(int,sys.stdin.readline().split())

graph_dict = {}

for _ in range(M):
    a_node, b_node = map(int,sys.stdin.readline().split())
    if a_node not in graph_dict:
        graph_dict[a_node] = [b_node]
    else:
        graph_dict[a_node].append(b_node)

    if b_node not in graph_dict:
        graph_dict[b_node] = [a_node]
    else:
        graph_dict[b_node].append(a_node)

visited = [False] * (N+1)
stack = [V]
dfs(stack,visited)

visited = [False] * (N+1)
queue = collections.deque([V])
bfs(queue,visited)