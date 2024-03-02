import sys
arr = []
for i in range(5):
    arr.append(sys.stdin.readline().rstrip())
answer = ''
for i in range(15):
    for j in range(5):
        if len(arr[j]) <= i:
            continue

        answer += arr[j][i]
print(answer)