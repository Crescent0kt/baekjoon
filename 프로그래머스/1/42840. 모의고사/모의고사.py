def solution(answers):
    answer = []
    #초기화
    one = 0
    two = 0
    three = 0
    #정답 배열 생성 
    two_arr = [1,3,4,5]
    three_arr = [3,1,2,4,5]
    for i,ans in enumerate(answers):
        if i%5 + 1 == ans:
            one += 1
        if (i%2 == 0 and ans == 2) or (i%2 != 0 and two_arr[(i//2) %4] == ans):
            two += 1
        if (three_arr[(i//2)%5] == ans):
            three +=1
    max_score = max(one,two,three)
    if one == max_score:
        answer.append(1)
    if two == max_score:
        answer.append(2)
    if three == max_score:
        answer.append(3)
    return answer