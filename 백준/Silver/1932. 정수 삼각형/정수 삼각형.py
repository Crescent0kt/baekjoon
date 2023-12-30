import sys
n = int(sys.stdin.readline())

arr = [0]* n
for i in range(n):
    nums = list(map(int,sys.stdin.readline().split()))
    for i in range(len(nums)-1,0,-1):
        arr[i] = max(arr[i-1],arr[i]) + nums[i]
    arr[0] += nums[0]

print(max(arr))