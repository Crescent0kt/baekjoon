def solution(clothes):
    a = {}
    for _, cloth in clothes:
        if cloth in a:
            a[cloth] += 1
        else:
            a[cloth] = 1
        count = 1
    for i in a:
        count *= (a[i] +1)
    
    
    
    return count-1