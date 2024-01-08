import sys

n = int(sys.stdin.readline())

stack = []

count = 1
ans = []
for _ in range(n):
    num = int(sys.stdin.readline())
    #같아질때 까지 넣음
    while count <= num:
        stack.append(count)
        ans.append("+")
        count += 1
    #같으면 저장
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    #다르면 나감
    else:
        print("NO")
        exit()

for s in ans:
    print(s)