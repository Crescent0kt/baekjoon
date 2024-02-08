def solution(n):
    answer = []
    def hanoi(n,answer,a,b,c):
        if n == 1:
            answer.append([a,c])
        else:
            hanoi(n-1, answer, a,c,b)
            answer.append([a,c])
            hanoi(n-1, answer, b,a,c)
    
    hanoi(n,answer,1,2,3)
    return answer