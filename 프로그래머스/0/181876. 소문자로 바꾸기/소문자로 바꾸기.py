def solution(myString):
    answer = ''
    for m in myString:
        if ord(m) >= ord('A') and ord(m) <= ord('Z'):
            answer += chr(ord('a') + ord(m) - ord('A'))
        else:
            answer += m
    return answer