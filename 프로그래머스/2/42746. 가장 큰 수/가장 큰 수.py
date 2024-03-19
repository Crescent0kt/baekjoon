from functools import cmp_to_key
def compare(x, y):
    if str(x) + str(y) > str(y) + str(x):
        return -1
    elif str(x) + str(y) < str(y) + str(x):
        return 1
    else:
        return 0
    
def solution(numbers):
    numbers.sort(key=cmp_to_key(compare))
    return str(int(''.join(map(str,numbers))))