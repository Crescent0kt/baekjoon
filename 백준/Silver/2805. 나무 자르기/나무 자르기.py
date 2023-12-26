import sys

n, m = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

# 설정할 최소, 최대 길이 -> 양이 늘어난다. r에 가까운게 정답
l = 0
r = max(arr)

ans = l
while l<=r:
    mid = (l+r)//2
    count = 0
    for i in range(n):
        cut = arr[i] - mid if arr[i] - mid >0 else 0
        count += cut
    if count >= m:
        ans = max(ans, mid)
        l = mid+1
    else:
        r = mid - 1

print(ans)

