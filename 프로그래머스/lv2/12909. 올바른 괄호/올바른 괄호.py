def solution(s):
    count = 0
    for a in s:
        if a =="(":
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count == 0:
        return True
    else: return False