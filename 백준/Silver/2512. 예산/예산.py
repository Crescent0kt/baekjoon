import sys

N = int(sys.stdin.readline())
req = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())

l, r = 0, max(req)
ans = 0

while l<=r:
    mid = (l+r)//2
    count = 0

    for i in range(len(req)):
        if req[i] < mid:
            count += req[i]
        else:
            count += mid

    if count<=budget:
        ans = max(mid,ans)
        l = mid+1
    else:
        r = mid -1


print(ans)