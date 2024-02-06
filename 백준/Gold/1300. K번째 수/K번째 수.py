import sys

N = int(sys.stdin.readline())
k  = int(sys.stdin.readline())
l = 1
r = N *N
answer  = 0
while l<=r:
    mid = (l+r)//2
    temp = 0
    for i in range(1,N+1):
        temp += min(N,mid//i)
    if temp >= k:
        ans = mid
        r = mid-1
    else:
        l = mid+1

print(ans)