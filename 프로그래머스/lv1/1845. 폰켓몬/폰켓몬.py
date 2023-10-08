def solution(nums):
    answer = 0
    nums.sort()
    check = nums[0]
    answer +=1
    for i in nums:
        if check != i:
            answer += 1
            check = i
    if answer > len(nums)//2 : answer =  len(nums)//2
    return answer