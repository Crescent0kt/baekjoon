from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 0
    q = deque()
    
    for truck_weight in truck_weights:
        while weight < truck_weight:
            print(q)
            w, t = q.popleft()
            time = max(t + bridge_length - 1,time)
            weight += w
            

        time += 1
        weight = weight - truck_weight
        q.append((truck_weight,time))
        
    w, t = q[-1]
    answer = bridge_length + t

    return answer