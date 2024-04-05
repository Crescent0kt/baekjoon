def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    l, r = 1, rocks[-1]
    
    while l<=r:
        mid = (l+r) //2
        count = 0
        dist = 0
        for i in range(len(rocks)):
            if rocks[i] - dist < mid:
                count += 1
                if count > n:
                    break
            else:
                dist = rocks[i]
        if count > n:
            r = mid - 1
        else:
            answer = max(mid, answer)
            l = mid + 1
            
    return answer