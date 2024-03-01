from collections import deque
def solution(numbers):
    
    answer = [0] * len(numbers)
    max = numbers[-1]
    Q = deque()
    Q.append(numbers[-1])
    answer[-1] = -1
    
    for i in range(len(numbers)-2,-1,-1):
        if numbers[i] >= max:
            max = numbers[i]
            Q = deque()
            Q.append(numbers[i])
            answer[i] = -1
        else:
            popL = Q.popleft()
            while popL <= numbers[i]:
                popL = Q.popleft()
        
            answer[i] = popL
            Q.appendleft(popL)
            Q.appendleft(numbers[i])
    
    return answer