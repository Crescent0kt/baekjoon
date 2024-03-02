import sys

num = int(sys.stdin.readline())
n  = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int,sys.stdin.readline().split())
    num = num - a*b
if num == 0:
    print("Yes")
else:
    print("No")