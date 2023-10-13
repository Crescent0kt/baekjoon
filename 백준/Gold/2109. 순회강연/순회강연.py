import sys

n = int(sys.stdin.readline())
if n != 0:
    arr = []
    #p -> 돈 , d -> due (p,d)
    for _ in range(n):
        arr.append(list(map(int,sys.stdin.readline().split())))

    arr.sort(key = lambda x : x[0], reverse = True)

    due = max(arr, key = lambda x: x[1])[1]
    #1 to N 금액저장
    dp = [0] *(due+1)

    #돈 많은 순서로 정렬된 값
    for p,d in arr:
        for j in range(d,0,-1):
            if dp[j] == 0:
                dp[j] = p
                break

    print(sum(dp))
else:
    print(0)