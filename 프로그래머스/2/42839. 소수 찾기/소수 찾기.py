from itertools import permutations

def solution(numbers):
    answer = 0
    
    # 에라토스테네스의 체를 사용한 소수 판별
    numbers_str = list(numbers)  # 문자열 리스트로 변환
    max_val = int(''.join(sorted(numbers_str, reverse=True)))
    
    arr = [False, False] + [True] * (max_val - 1)
    
    for i in range(2,int(max_val**0.5) + 1):
        if arr[i] == True:
            j = i+i
            while j<=max_val:
                arr[j] = False
                j += i
                
    # 가능한 모든 숫자 조합 생성 및 소수 판별
    candidates = set()
    
    for i in range(len(numbers)):
        temp_nums = list(map(int, map(''.join, permutations(numbers_str, i+1))))
        candidates.update(temp_nums)
        
    for num in candidates:
        if arr[num]:
            answer += 1
            
    return answer