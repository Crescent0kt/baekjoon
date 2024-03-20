def solution(progresses, speeds):
    answer = []
    i = 0
    j = 0
    while j < len(progresses):
        if progresses[j] + speeds[j] * i >= 100:
            count = 0
            while j+count < len(progresses) and progresses[j+count] + speeds[j+count] * i >= 100:
                count += 1
            
            answer.append(count)
            j += count
            
        else:
            i += 1
    
    return answer