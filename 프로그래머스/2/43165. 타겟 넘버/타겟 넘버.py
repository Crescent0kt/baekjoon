from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((numbers[0],1))
    q.append((-numbers[0],1))

    while q:
        num, co = q.popleft()
        if co == len(numbers):
            if num == target:
                answer +=1
            continue
        
        q.append((num+numbers[co],co+1))
        q.append((num-numbers[co],co+1))
                    
    return answer