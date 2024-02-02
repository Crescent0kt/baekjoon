import sys
N, C = map(int,sys.stdin.readline().split())

houses = []
for i in range(N):
    houses.append(int(sys.stdin.readline()))

houses.sort()

l, r = 1, houses[-1] - houses[0]
result = 0

while l<=r:
    mid = (l+r)//2
    count = 1
    a = 0

    for i in range(1,N):
        if houses[i] - houses[a]>= mid:
            count +=1
            a = i

    if count >= C:
        result = max(result, mid)
        l = mid+1
    else:
        r = mid -1
print(result)