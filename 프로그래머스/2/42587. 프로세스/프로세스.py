from collections import deque
def solution(priorities, location):
    answer = 0
    arr = deque([(p, i) for i, p in enumerate(priorities)])
    
    while arr:
        if arr[0][0] < max(p[0] for p in arr):
            arr.append(arr.popleft())
        else:
            answer += 1
            if arr.popleft()[1] == location:
                return answer