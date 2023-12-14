import sys
import collections
N = int(sys.stdin.readline())

stack = collections.deque(x+1 for x in range(N))

while len(stack) >1:
    stack.popleft()
    stack.append(stack.popleft())

print(stack.pop())