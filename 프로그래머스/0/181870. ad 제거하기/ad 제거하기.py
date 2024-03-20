def solution(strArr):
    answer = []
    for str in strArr:
        for i,s in enumerate(str):
            if i < len(str)-1 and s == "a" and str[i+1] == "d":
                break
        else:
            answer.append(str)    
    return answer