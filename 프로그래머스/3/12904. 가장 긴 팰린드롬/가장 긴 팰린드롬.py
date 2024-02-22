def solution(s):
    answer = 0
    if not s:
        return answer
    for i in range(len(s)):
        #홀수 감지
        count_odd = 1
        j = 1
        while i-j>=0 and i+j<=len(s)-1 and s[i-j] == s[i+j]:
            count_odd += 2
            j += 1
            
        
        #짝수 감지
        count_even = 0
        j = 1
        
        while i-j+1>=0 and i+j<=len(s)-1 and  s[i-j+1] == s[i+j]:
            count_even += 2
            j+= 1
            
        answer = max(answer, count_odd, count_even)
    return answer