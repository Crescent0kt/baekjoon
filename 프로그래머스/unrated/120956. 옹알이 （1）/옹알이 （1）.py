def solution(babbling):
    answer = 0
    for bab in babbling:
        t= bab
        check = True
        while check != False:
            check = False
            if t[:3] == "aya":
                t = t[3:]
                check = True
            elif t[:2] == "ye":
                t = t[2:]
                check = True
            elif t[:3] == "woo":
                t = t[3:]
                check = True
            elif t[:2] == "ma":
                t = t[2:]
                check = True
        else:
            if t == "":
                answer+=1
    return answer