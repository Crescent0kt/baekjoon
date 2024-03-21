def solution(sizes):
    mx1=0
    mx2 = 0
    for w,h in sizes:
        mx1 = max(mx1,w,h)
        mx2 = max(mx2,min(w,h))
        
    return mx1 * mx2