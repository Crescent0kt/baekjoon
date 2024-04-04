def solution(n, times):
    answer = 0
    l, r = 1, max(times) * n
    
    while l<=r:
        mid = (l+r)//2
        cnt = 0
        for time in times:
            cnt += mid//time
            if cnt>=n:
                break
        
        if cnt >= n:
            answer = mid
            r = mid -1
        else:
            l = mid + 1
    return answer