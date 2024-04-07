import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
count = 0

for i in range(N):
    start = 0
    end = N - 1
    while start < end:
        if start == i:  # 현재 i와 같은 인덱스면 start를 오른쪽으로 이동
            start += 1
            continue
        if end == i:  # 현재 i와 같은 인덱스면 end를 왼쪽으로 이동
            end -= 1
            continue
        current_sum = arr[start] + arr[end]
        if current_sum == arr[i]:
            count += 1
            break
        elif current_sum < arr[i]:
            start += 1
        else:
            end -= 1

print(count)