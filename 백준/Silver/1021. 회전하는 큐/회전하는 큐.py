import sys
from collections import deque

#큐의 크기, 뽑을 숫자 수
N,M = map(int,sys.stdin.readline().split())

#큐 생성
q = deque(x for x in range(1,N+1))
cursor = 0
ans = 0
nums = list(map(int,sys.stdin.readline().split()))
#뽑을 숫자 만큼 반복
for i in range(M):
    num = nums[i]
    #왼쪽 이동 확인
    l_cursor = cursor
    l_count = 0
    while q[l_cursor] != num:
        l_count += 1
        l_cursor -= 1
        if l_cursor < 0:
            l_cursor = len(q)-1

    #오른쪽 이동
    r_cursor = cursor
    r_count = 0
    while q[r_cursor] != num:
        r_count += 1
        r_cursor += 1
        if r_cursor == len(q):
            r_cursor = 0

    #둘 중 이동 수 작은 거 비교
    ans += min(r_count,l_count)
    q.remove(num)
    cursor = l_cursor
    if cursor == len(q):
        cursor = 0

print(ans)