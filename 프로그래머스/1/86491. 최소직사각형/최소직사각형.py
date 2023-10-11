def solution(sizes):
    max_small = 0
    max_large = 0
    
    for i in sizes:
        small,large = sorted(i)
        
        if max_small < small:
            max_small = small
        if max_large < large:
            max_large = large
        
    return max_small * max_large