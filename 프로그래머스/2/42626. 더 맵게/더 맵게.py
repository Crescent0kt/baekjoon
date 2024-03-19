import heapq
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while True:
        a = heapq.heappop(scoville)
        if a < K:
            if scoville:
                b = heapq.heappop(scoville) * 2
                heapq.heappush(scoville,a+b)
                answer += 1
            else:
                return -1
        else:
            break
    return answer