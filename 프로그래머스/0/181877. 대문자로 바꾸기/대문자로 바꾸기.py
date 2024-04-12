def solution(myString):
    answer = ''
    for m in myString:
        if ord(m) >= ord('a') and ord(m) <= ord('z'):
            answer += chr(ord('A') + ord(m) - ord('a'))
        else:
            answer += m
    return answer