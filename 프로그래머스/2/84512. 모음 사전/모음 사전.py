def solution(word):
    answer = 0
    wo = ["","A","E","I","O","U"]
    wordarr = []
    for i in range(1,6):
        
        for j in range(6):
            if j == 0:
                answer += 1
                if word == wo[i] :
                    return answer
                continue
                
            for k in range(6):
                if k == 0:
                    answer += 1
                    if word == wo[i]+wo[j]:
                        return answer
                    continue 
                
                for l in range(6):
                    if l == 0:
                        answer += 1
                        if word == wo[i]+wo[j]+wo[k]:
                            return answer
                        continue
                    
                    for m in range(6):
                        answer += 1
                        if word == wo[i]+wo[j]+wo[k]+wo[l]+wo[m]:
                            return answer
    return answer