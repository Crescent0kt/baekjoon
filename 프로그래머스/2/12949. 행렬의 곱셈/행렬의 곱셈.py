def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        tmparr = []
        for j in range(len(arr2[0])):
            ans  = 0
            for k in range(len(arr1[0])):
                ans += arr1[i][k] * arr2[k][j]
            tmparr.append(ans)
        answer.append(tmparr)
    
    return answer