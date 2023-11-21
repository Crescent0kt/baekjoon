from itertools import combinations

def solution(numbers):
    ans = []
    num_list = combinations(numbers,2)
    for a, b in num_list:
        ans.append(a+b)
    
    answer = list(set(ans))
    answer.sort()
    return answer