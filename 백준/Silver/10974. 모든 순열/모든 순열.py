from itertools import permutations

N = int(input())
a = permutations(range(1,N+1),N)

for i in a:
    print(*i)