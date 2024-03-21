from collections import defaultdict
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(len(computers)):
        if visited[i]:
            continue
        answer += 1
        arr = [i]
        visited[i] = True
        
        while arr:
            j = arr.pop()
            for k in range(len(computers[j])):
                if j == k:
                    continue
                if computers[j][k] ==1 and visited[k] != True:
                    arr.append(k)
                    visited[k] = True

    return answer