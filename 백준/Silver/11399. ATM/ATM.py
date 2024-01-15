import sys

N =int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()
ans = 0
time =0
for i in range(N):
    time = time+arr[i]
    ans = ans + time

print(ans)