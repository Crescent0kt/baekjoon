from collections import defaultdict
def solution(phone_book):
    dic = defaultdict(dict)
    for phone in phone_book:
        phonedict = dic
        #첫 값 부터 없으면 그대로 쭉 만들기
        if phone[0] not in phonedict:
            for i in range(len(phone)):
                phonedict[phone[i]] = {}
                phonedict = phonedict[phone[i]]
        else:
            # 첫 값이 있는 경우
            check = False
            phonedict = phonedict[phone[0]]

            for i in range(1,len(phone)):
                if check:
                    phonedict[phone[i]] = {}
                    phonedict = phonedict[phone[i]]
                else:   
                    if phone[i] in phonedict:    
                        phonedict = phonedict[phone[i]]
                    else:
                        if not phonedict:
                            return False
                        else:
                            check = True
                            phonedict[phone[i]] = {}
                            phonedict = phonedict[phone[i]]
            else:   
                if not check:
                    return False
    return True