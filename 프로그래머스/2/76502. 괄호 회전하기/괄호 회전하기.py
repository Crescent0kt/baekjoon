def solution(s):
    answer = 0
    for i in range(len(s)):
        arr = []
        check = True
        for j in range(i,len(s)):
            if s[j] == '[' or s[j] == '(' or s[j] == '{':
                arr.append(s[j])
            else:
                if len(arr) == 0 :
                    check = False
                    break
                a = arr.pop()
                if a == "[":
                    if s[j] != "]":
                        check = False
                        break
                elif a == "(":
                    if s[j] != ")":
                        check = False
                        break
                else:
                    if s[j] != "}":
                        check = False
                        break


        if check:
            for j in range(i):
                if s[j] == '[' or s[j] == '(' or s[j] == '{':
                    arr.append(s[j])
                else:
                    if len(arr) == 0 :
                        check = False
                        break
                    a = arr.pop()
                    if a == "[":
                        if s[j] != "]":
                            check = False
                            break
                    elif a == "(":
                        if s[j] != ")":
                            check = False
                            break
                    elif a == "{":
                        if s[j] != "}":
                            check = False
                            break

        if len(arr) == 0 and check:
            answer +=1
    return answer