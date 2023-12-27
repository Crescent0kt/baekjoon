import sys

#듣 ㄴ, 보 ㄴ
n,m = map(int,sys.stdin.readline().split())
a = set()
b = set()
for i in range(n):
    a.add(sys.stdin.readline().rstrip())

for _ in range(m):
    b.add(sys.stdin.readline().rstrip())

c = []
for aa in a:
    if aa in b:
        c.append(aa)

print(len(c))
c.sort()
for cc in c:
    print(cc)