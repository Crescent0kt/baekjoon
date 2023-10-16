import sys

N, K = map(int,sys.stdin.readline().split())
people = list(map(int,sys.stdin.readline().split()))
arr = [0] * (N-1)

for i in range(N-1):
    arr[i] = people[i+1] - people[i]

arr.sort()
ANSWER = 0
for i in range(N-K):
    ANSWER += arr[i]
print(ANSWER)