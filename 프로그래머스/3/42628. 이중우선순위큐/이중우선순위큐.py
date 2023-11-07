import heapq
def solution(operations):
    answer = []
    for oper in operations:
        order, num = oper.split()
        if order =="I":
            heapq.heappush(answer,int(num))
        elif order =="D":           
            if len(answer) !=0:
                if num == "1":
                    answer.remove(max(answer))
                    heapq.heapify(answer)
                else:
                    heapq.heappop(answer)
    
    #[최대, 최소] or [0, 0]
    if len(answer) == 0:
        return [0,0]
    else:
        return [max(answer), answer[0]]