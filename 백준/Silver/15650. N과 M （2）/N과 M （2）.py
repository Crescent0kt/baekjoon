"""
N까지 자연수에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
"""
import sys
from itertools import combinations
N,M = map(int,sys.stdin.readline().split())

arr = [i for i in range(1,N+1)]

ans = combinations(map(str,arr), M)

for a in ans:
    print(' '.join(a))
