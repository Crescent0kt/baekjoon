from collections import deque
def solution(prices):
    answer = deque()
    arr = []
    for i,p in enumerate(prices):
        while arr:
            pp, ii = arr[-1]
            if pp > p:
                arr.pop()
                prices[ii] = i-ii
            else:
                break
        arr.append((p,i))
    
    while arr:
        p,i = arr.pop()
        prices[i] = len(prices)-1-i
        
    return prices