import sys
import math
T = int(sys.stdin.readline())

for _ in range(T):
    PS = sys.stdin.readline().rstrip()
    stack = []
    for s in PS:
        if s =="(":
            stack.append("(")
        else:
            if not stack:
                print("NO")
                break
            else:
                stack.pop()
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
