import sys

N = int(sys.stdin.readline())

pay = list(map(int, sys.stdin.readline().split()))

money = int(sys.stdin.readline())

pay.sort()

max_num = 0
for i,p in enumerate(pay):
    if p > money/(N-i):
        max_num = money//(N-i)
        break
    else:
        max_num = p
    money = money - max_num

print(max_num)