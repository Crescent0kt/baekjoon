def solution(nums):
    answer = 0
    num_set = set([])
    N = len(nums)//2
    for num in nums:
        num_set.add(num)
    
    if len(num_set) < N:
        return len(num_set)
    else:
        return N
    