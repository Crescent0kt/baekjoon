n = int(input())
t = []
p = []
dp = [0] * (n + 1)  # dp 테이블 초기화

for _ in range(n):
    time, pay = map(int, input().split())
    t.append(time)
    p.append(pay)

# 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    if t[i] + i <= n:  # 상담이 퇴사 전에 끝나는 경우
        # i일에 상담을 진행할 경우 i일에 받을 수 있는 금액과
        # 상담이 끝난 후의 날짜의 최대 수익을 합친 것과
        # i일에 상담을 진행하지 않을 경우의 최대 수익을 비교
        dp[i] = max(p[i] + dp[i + t[i]], dp[i + 1])
    else:  # 상담이 퇴사 전에 끝나지 않는 경우
        dp[i] = dp[i + 1]

print(dp[0])
