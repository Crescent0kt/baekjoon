from itertools import permutations

def solution(k, dungeons):
    n = len(dungeons)
    answer = 0

    for order in permutations(range(n)):
        energy = k
        count = 0
        for i in order:
            if dungeons[i][0] <= energy:
                energy -= dungeons[i][1]
                count += 1
            else:
                break
        answer = max(answer, count)
        
    return answer
