def solution(n, lost, reserve):
    answer = 0
    arr = [1] * (n+1)
    for l in lost:
        arr[l] -= 1
    
    for r in reserve:
        arr[r] += 1
    
    for i in range(1,n+1):
        if arr[i] == 2:
            if arr[i-1] == 0:
                arr[i] -= 1
                arr[i-1] += 1
            elif i != n and arr[i+1] == 0:
                arr[i] -= 1
                arr[i+1] += 1
    for i in range(1, n+1):
        if arr[i] > 0:
            answer += 1
    return answer