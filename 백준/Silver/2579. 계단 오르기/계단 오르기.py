import sys

n = int(sys.stdin.readline())

s = list(int(sys.stdin.readline()) for _ in range(n))

if n <= 2:
    print(sum(s))
else:
    dp = [0] * n
    dp[0] = s[0]
    dp[1] = s[1] + s[0]

    for i in range(2,n):
        dp[i] = max(dp[i-2] + s[i], dp[i-3]+s[i-1]+s[i])
    print(dp[n-1])
