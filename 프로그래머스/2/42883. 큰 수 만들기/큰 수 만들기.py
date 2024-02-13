def solution(number, k):
    
    answer = [number[0]]
    cursor = 1
    while k >0 and cursor <len(number) :
        while k>0 and len(answer) != 0:
            if number[cursor] > answer[-1]:
                answer.pop()
                k -= 1
            else:
                break
        answer.append(number[cursor])
        cursor += 1
        
        if cursor == len(number):
            while k>0:
                answer.pop()
                k -= 1
        elif k == 0:
            while cursor<len(number):
                answer.append(number[cursor])
                cursor+= 1
        
    return ''.join(answer)
