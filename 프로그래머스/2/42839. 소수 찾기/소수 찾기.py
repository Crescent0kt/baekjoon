import math
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    num_set = set()
    for i in range(1,len(numbers)+1):
        num_arr = permutations(numbers, i)
        for num in num_arr:
            num_set.add(int(''.join(num)))
            
    for num in num_set:
        if is_prime(num):
            answer +=1 
    
    return answer