#for 돌면서 
def solution(progresses, speeds):
    answer = []
    check = 0
    N = len(progresses)
    while check < N:
        count = 0
        for i in range(N):
            progresses[i] += speeds[i]
        while check < N and progresses[check] >= 100:
            count += 1
            check += 1
        if count != 0 : answer.append(count)
        
    return answer