import math

def solution(k, d):
    count = 0

    for x in range(d//k+1):
        y_max = math.floor(math.sqrt(d**2 - (k*x)**2)/k)
        count += y_max + 1
        
    return count