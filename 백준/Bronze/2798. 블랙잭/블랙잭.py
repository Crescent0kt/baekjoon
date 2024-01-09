from itertools import combinations

N,M = map(int,input().split())

Arr = combinations(map(int,input().split()),3)
minsum = 0
for i in Arr:
    if sum(i) >minsum and sum(i) <= M:
        minsum = sum(i)
    
print(minsum)