def solution(s):
    answer = True
    arr = []
    for ss in s:
        if ss == "(":
            arr.append("(")
        else:
            if arr:
                arr.pop()
            else:
                return False
    if not arr:
        return True
    else:
        return False