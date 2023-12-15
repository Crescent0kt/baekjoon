import sys

N,M = map(int,sys.stdin.readline().split())
d = {}
for _ in range(N):
    url, password = sys.stdin.readline().split()
    d[url] = password

for _ in range(M):
    url = sys.stdin.readline().strip()
    print(d[url] if url in d else "")
