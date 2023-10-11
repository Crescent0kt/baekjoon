from collections import deque
def solution(numbers, target):
    answer = 0

    dq = deque()
    dq.append(numbers[0])
    dq.append(-numbers[0])
    for i in range(1,len(numbers)):
        #홀짝
        count = 2**i
        while count != 0:
            num = dq.popleft()
            dq.append(num + numbers[i])
            dq.append(num - numbers[i])
            count -= 1
    for j in dq:
        if j == target:
            answer+=1
    
    return answer