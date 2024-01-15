#현재 배열 값(현재 계단에서의 최고점)
#현재 계단에서의 최고값 -> 뛰어서 한칸전에서 나까지오기 or 뛰어서 나한테오기
import sys
N = int(sys.stdin.readline())

stair = [0]
for _ in range(N):
    stair.append(int(sys.stdin.readline()))

if len(stair) == 2:
    print(stair[-1])
    exit()
ans = [0] * (N+1)
ans[1] = stair[1]
ans[2] = stair[1] + stair[2]

for i in range(3,N+1):
    ans[i] = stair[i] + max(ans[i-2], ans[i-3]+stair[i-1])

print(ans[-1])