"""
1. 가장 작은 생성자는 N보다 작아야 한다.
2. 자리수 * 9 (ex 3자리 => 27) 보다 작을 수 없음
"""

import sys

N = int(sys.stdin.readline())
len_n =  len(str(N))
for i in range(N-(len_n * 9),N):
    num = i
    ans = num
    while num>0:
        ans += num%10
        num = num//10
    
    if ans == N:
        print(i)
        break
else:
    print(0)