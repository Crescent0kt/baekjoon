def solution(clothes):    
    answer = 1
    dic = {}
    for clo,category in clothes:
        if category not in dic:
            dic[category] = 1
        else:
            dic[category] += 1
    
    for key in dic.keys():
        answer = answer * (dic[key] + 1)
    
    return answer -1