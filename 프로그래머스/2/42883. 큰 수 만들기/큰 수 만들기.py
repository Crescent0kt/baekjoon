def solution(number, k):
    answer = ''
    stack = []
    numbers = list(map(int,number))
    
    for tmp in numbers:
        while k!=0 and len(stack) !=0:
            if tmp > stack[-1]:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(tmp)
    while k != 0:
        k -= 1
        stack.pop()
    answer += ''.join(str(_) for _ in stack)
    return answer