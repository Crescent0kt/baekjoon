def solution(answers):
    answer = [0,0,0]
    sol_a = [1,2,3,4,5]
    sol_b = [2,1,2,3,2,4,2,5]
    sol_c = [3,3,1,1,2,2,4,4,5,5]
    
    
    for i,ans in enumerate(answers):
        if ans == sol_a[i%len(sol_a)]:
            answer[0] += 1
        if ans == sol_b[i%len(sol_b)]:
            answer[1] += 1
        if ans == sol_c[i%len(sol_c)]:
            answer[2] +=1
    a = []
    max_score = max(answer)
    for i,n in enumerate(answer):
        if n == max_score:
            a.append(i+1)
    return a