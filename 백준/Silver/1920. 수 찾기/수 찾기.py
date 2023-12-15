import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
num_dict = {}

for a in A:
    num_dict[a] = 1

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for b in B:
    print(num_dict.get(b,0))