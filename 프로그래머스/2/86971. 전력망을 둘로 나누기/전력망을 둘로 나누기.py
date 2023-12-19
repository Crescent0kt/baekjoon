from collections import defaultdict
def solution(n, wires):
    tree = defaultdict(list)
    minimum = n
    for wire in wires:
        tree[wire[0]].append(wire[1])
        tree[wire[1]].append(wire[0])
    
    for wire in wires:
        visited = [False]*(n+1)
        tree[wire[0]].remove(wire[1])
        tree[wire[1]].remove(wire[0])
        
        count1 = 1
        stack = [wire[0]]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                count1 += 1
                for neighbor in tree[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        
        count2 = 1
        stack = [wire[1]]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                count2 += 1
                for neighbor in tree[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        minimum = min(minimum, abs(count1-count2))
        tree[wire[0]].append(wire[1])
        tree[wire[1]].append(wire[0])
    
    return minimum