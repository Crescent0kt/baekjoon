import sys

N = int(sys.stdin.readline())

cows = []

for _ in range(N):
    hour, minute, second = map(int,sys.stdin.readline().split())
    time = hour*3600 + minute * 60 + second
    cows.append((time,hour,minute,second))

cows.sort()
for cow in cows:
    print(cow[1],cow[2],cow[3])