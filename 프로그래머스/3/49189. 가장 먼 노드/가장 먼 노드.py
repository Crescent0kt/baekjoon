from collections import defaultdict
from collections import deque
def solution(n, edge):
    inf = int(10e9)
    visited = [inf] * (n+1)
    graph = defaultdict(list)
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    arr = deque()
    arr.append((1,0))
    visited[1] = 0
    max_count = 0
    while arr:
        node, cost = arr.popleft()
        
        if cost > visited[node]:
            continue
        
        max_count = max(max_count,cost)
        
        for next_node in graph[node]:
            if cost+1 < visited[next_node]:
                visited[next_node] = cost+1
                arr.append((next_node, cost+1)) 
    
    answer = 0
    for i in range(1,len(visited)):
        if visited[i] == max_count:
            answer += 1
    print(visited)
    return answer
        