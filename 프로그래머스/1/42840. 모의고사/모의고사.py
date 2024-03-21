def solution(answers):
    answer = []
    loser1 = [1, 2, 3, 4, 5]
    loser2 = [2, 1, 2, 3, 2, 4, 2, 5]
    loser3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score1 = 0
    score2 = 0
    score3 = 0
    for i,ans in enumerate(answers):
        if ans == loser1[i%len(loser1)]:
            score1 += 1
        if ans == loser2[i%len(loser2)]:
            score2 += 1
        if ans == loser3[i%len(loser3)]:
            score3 += 1
    
    max_score = max(score1,score2,score3)
    if max_score == score1:
        answer.append(1)
    if max_score == score2:
        answer.append(2)
    if max_score == score3:
        answer.append(3)
           
    return answer