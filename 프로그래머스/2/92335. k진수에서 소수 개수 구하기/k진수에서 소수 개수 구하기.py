import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = ""
    while n>k:
        num = str(n%k) + num
        n = n//k
    else:
        num = str(n%k) + num
    items = str(num).split("0")
    for item in items:
        if item == "" or item =="1":
            continue
        num_item = int(item)
        if is_prime(num_item) == True:
            answer += 1
    return answer