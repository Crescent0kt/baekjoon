import sys

T = int(sys.stdin.readline())

for _ in range(T):
    start, end = map(int,sys.stdin.readline().split())
    distance = end- start
    max_num = 1
    count = 0
    while distance>=2*max_num:
        distance = distance - (2*max_num)
        count = count+2
        max_num = max_num+1

    while distance:
        if max_num<=distance:
            count = count+1
            distance = distance-max_num
        else:
            max_num = max_num-1

    print(count)
