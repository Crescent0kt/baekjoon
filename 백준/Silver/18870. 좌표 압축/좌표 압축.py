import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

dict = {}
arr2 = sorted(list(set(arr)))

for i in range(len(arr2)):
    dict[arr2[i]] = i

for a in arr:
    print(dict[a], end = " ")