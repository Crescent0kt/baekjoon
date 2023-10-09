def solution(triangle):

    N = len(triangle)
    D = [0] * (N)
    D[0] = triangle[0][0]
    
    for i in range(1,N):
        tmp = D[:i]
        list = triangle[i]
        D[0] = tmp[0] + list[0]
        D[i] = tmp[i-1] + list[i]
        
        for j in range(1,i):
            D[j] = max(tmp[j-1],tmp[j]) + list[j]
            
    
    return max(D)