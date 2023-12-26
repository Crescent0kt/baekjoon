import sys

n, m = map(int,sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

l ,r = min(arr), max(arr) * m
ans = r

while l<=r:
    mid = (l+r) //2
    count =0
    for i in range(n):
        count += mid // arr[i]
    if count >= m:
        r = mid - 1
        ans = min(ans, mid)
        
    else:
        l = mid+ 1
print(ans)