def solution(phone_book):

    #딕셔너리에 저장
    dict = {}
    for phone in phone_book:
        dict[phone] = 1
    
    for phone in phone_book:
        s = ""
        #핸드폰 번호 각자리
        for phone_s in phone:
            s += phone_s
            if s in dict and s != phone:
                return False
    return True