import sys

N, M = map(int,sys.stdin.readline().split())

woods = list(map(int,sys.stdin.readline().split()))
l = 0
r = max(woods)

ans = 0
while l<=r:
    mid = (l+r)//2
    sum_wood = 0
    for wood in woods:
        if wood - mid >0:
            sum_wood += (wood-mid)
    if M <= sum_wood:
        ans = max(ans, mid)
        l = mid + 1
    else:
        r = mid -1

print(ans)