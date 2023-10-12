def solution(brown, yellow):
    answer = []
    brown = brown -4
    
    i = 1
    while True :
        if yellow%i ==0:
            if yellow/i * 2 + 2*i == brown:
                answer = [(yellow/i) +2, i+2]
                break
        i += 1
        if i > yellow **(0.5) : break
    return answer