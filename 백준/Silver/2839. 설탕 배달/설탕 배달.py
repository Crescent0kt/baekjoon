import sys
INF = int(10e9)
def func(N):

    arr = [INF,INF,1,INF,1]
    for i in range(5,N):
        num = min(arr[i-3] + 1, arr[i-5] + 1)
        arr.append(num)
    return arr[N-1]

N = int(sys.stdin.readline())
num = func(N)
if num >= INF:
    print(-1)
else:
    print(num)
