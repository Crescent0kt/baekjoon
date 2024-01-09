import sys
#저장
N,K = map(int,sys.stdin.readline().split())
#배열생성
arr = [x+1 for x in range(N)]
#정답 배열
ans = []
#커서 두고 -> 도착했을 때 해당 커서위치한 값 지움
cursor = 0
for i in range(N):
    cursor = (cursor+(K-1)) % len(arr)
    ans.append(arr.pop(cursor))

print('<'+", ".join(map(str, ans)) + ">")
