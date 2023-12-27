import sys
#k개의 랜선 -> n개로 만들고 싶어요
k, n = map(int, sys.stdin.readline().split())
lans = []

for _ in range(k):
    lans.append(int(sys.stdin.readline()))

ans = 0
#최대 길이, 최소 길이
l, r = 1, max(lans)

while l<=r:
    mid = (l+r)//2
    count = 0
    for lan in lans:
        count += lan//mid

    if count >= n:
        ans = max(ans,mid)
        l = mid+1
    else:
        r = mid-1
print(ans)