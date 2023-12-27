import sys
from collections import defaultdict
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    wear = defaultdict(list)
    for _ in range(n):
        a,b = sys.stdin.readline().split()
        wear[b].append(a)

    ans = 1
    for val in wear.values():
        ans = ans*(len(val)+1)

    print(ans-1)