from collections import defaultdict
import heapq
def solution(n, costs):
    inf = int(10e9)
    dic = defaultdict(list)
    
    for a,b,c in costs:
        dic[a].append((b,c))
        dic[b].append((a,c))
    
    arr = []
    arr.append((0,0))
    visited = [False] * n
    total = 0
    while arr:
        cost, node = heapq.heappop(arr)
        if visited[node]:
            continue
        total += cost
        visited[node] = True
        for next_node,next_cost in dic[node]:
            heapq.heappush(arr,(next_cost,next_node))
    
    return total