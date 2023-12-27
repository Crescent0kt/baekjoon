import sys
#k개의 랜선 -> n개로 만들고 싶어요
n, c = map(int, sys.stdin.readline().split())

house = []
for _ in range(n):
    house.append(int(sys.stdin.readline()))

house.sort()

#공유기 최소 거리 1, 최대 거리 max - min
l, r = 1, house[-1] - house[0]
ans = 0

while l<=r:
    mid = (l+r)//2
    count = 1
    a = 0
    for i in range(1,n):
        if house[i] - house[a]>= mid:
            count +=1
            a = i

    if count>=c:
        ans = max(ans, mid)
        l = mid+1
    else:
        r = mid-1
print(ans)