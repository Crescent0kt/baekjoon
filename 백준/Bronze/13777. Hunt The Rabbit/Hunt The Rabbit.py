import sys

while True:
    ans = int(sys.stdin.readline())
    if ans == 0:
        break

    l, r = 1,50

    while l<=r:
        mid = (l+r)//2
        print(mid, end =" ")
        if ans == mid:
            break

        if ans > mid:
            l = mid+1
        else:
            r = mid -1
    print("")