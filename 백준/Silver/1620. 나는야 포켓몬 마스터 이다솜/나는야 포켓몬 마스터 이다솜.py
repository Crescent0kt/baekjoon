import sys

#도감 수록 포켓몬, 맞출 문제 수
n,m = map(int,sys.stdin.readline().split())
dict = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    num = str(i+1)
    dict[num] =name
    dict[name] = num

for _ in range(m):
    q = sys.stdin.readline().rstrip()
    print(dict[q])