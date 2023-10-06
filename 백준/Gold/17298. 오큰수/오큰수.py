N = int(input())

A = list(map(int,input().split()))

stack = []
ans = [-1] * N
stack.append(0)

for i in range(1,N):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
    stack.append(i)

print(*ans)