import sys
from collections import deque
T = int(sys.stdin.readline())

for i in range(T):
    N,M = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    dq = deque((li[j], j) for j in range(N))

    count = 1
    while len(dq)>1:
        if dq[0][0] != max(dq, key =lambda x :x[0])[0]:
            a = dq.popleft()
            dq.append(a)
        else:
            val, index = dq.popleft()
            if index == M:
                print(count)
                break
            count += 1
    else:
        print(count)