def solution(cap, n, deliveries, pickups):
    answer = 0
    i = n-1
    j = n-1 
    
    while i>=0 or j>=0:
        ii = jj = -1
        
        x = cap
        while i>=0 and x >0:
            delivery = deliveries[i]
            if delivery>0 and ii == -1:
                ii = i
            if x >= delivery:
                x -= delivery
                deliveries[i] -= delivery
                i -= 1
            else:
                deliveries[i] -= x
                x =0

        x = cap
        while j>=0 and x >0:
            pickup = pickups[j]
            if pickup>0 and jj == -1:
                jj = j
            if x >= pickup:
                x -= pickup
                pickups[j] -= pickup 
                j -= 1
            else:
                pickups[j] -= x
                x = 0
                
        answer += 2*max(ii+1,jj+1)
    
    return answer