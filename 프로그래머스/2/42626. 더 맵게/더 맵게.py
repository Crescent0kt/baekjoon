import heapq
def solution(scoville, K):
    answer = 0
    scoville.sort()
    

    while scoville[0]<K and len(scoville) >=2:
        answer += 1
        min1 = heapq.heappop(scoville)   
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville,min1+(2*min2))
    
    if scoville[0] <K: return -1
    else: return answer