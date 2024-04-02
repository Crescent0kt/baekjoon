def solution(triangle):
    len_t = len(triangle)
    arr = [0] * len_t
    
    for i, nums in enumerate(triangle):
        if i == 0:
            arr[0] = nums[0]
            continue
        
        arr[i] = arr[i-1] + nums[i]
        
        for j in range(i-1, 0, -1):
            arr[j] = max(arr[j], arr[j-1]) + nums[j]

        arr[0] = arr[0] + nums[0]
    print(arr)
    return max(arr)