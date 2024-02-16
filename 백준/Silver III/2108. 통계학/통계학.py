import sys
from collections import Counter
N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()
freq = Counter(arr).most_common()
if len(freq) > 1 and freq[0][1] == freq[1][1]:
    mode = freq[1][0]
else:
    mode = freq[0][0]


print(round(sum(arr) / N))
print(arr[N//2])
print(mode)
print(arr[-1] - arr[0])