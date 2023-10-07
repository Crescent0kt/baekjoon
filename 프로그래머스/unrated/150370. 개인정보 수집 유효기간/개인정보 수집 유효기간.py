def solution(today, terms, privacies):
    answer = []
    year,month,day = map(int,today.split("."))
    tdy = 12*28*year + 28*month + day

    termsArr = {}
    for term in terms:
        a,b = term.split()
        termsArr[a] = b
    
    for i in range(len(privacies)):
        p_time, p_term = privacies[i].split()
        p_year, p_month, p_day = map(int,p_time.split("."))
        p = p_year * 12 * 28 + (p_month+int(termsArr[p_term])) * 28 + p_day

        if (tdy - p >= 0):
            answer.append(i+1)
                                
    return answer