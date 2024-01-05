import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x,y = map(int,sys.stdin.readline().split())
    dist = y-x
    i=1
    ans = 0
    #1. 대칭 이동
    while 2*i <= dist:
        ans += 2
        dist = dist - 2 * i
        i += 1
    #단일이동
    while dist > 0:
        if i > dist:
            i-=1
        else:
            dist = dist - i
            ans += 1

    print(ans)