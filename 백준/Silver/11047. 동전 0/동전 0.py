"""
크기 순 정렬하고 뒤에서부터 하나씩 빼서 카운팅
조건에 다음값은 무조건 배수라고 써져있으므로 , 정렬 필요없음 + 무조건 답 나옴
"""

import sys

N,K = map(int,sys.stdin.readline().split())

coins = []
count = 0
cursor = len(coins)-1
for _ in range(N):
    coins.append(int(sys.stdin.readline()))


while K>0:
    if K>=coins[cursor]:
        K -= coins[cursor]
        count +=1
    else:
        cursor -= 1

print(count)