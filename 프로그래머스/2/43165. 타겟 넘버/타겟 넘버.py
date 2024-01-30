def solution(numbers, target):
    answer = 0
    stack = [(numbers[0],1),(-numbers[0],1)]
    while stack:
        num, co = stack.pop()
        if co == len(numbers):
            if num == target:
                answer +=1
            continue
        
        stack.append((num+numbers[co],co+1))
        stack.append((num-numbers[co],co+1))
                    
    return answer