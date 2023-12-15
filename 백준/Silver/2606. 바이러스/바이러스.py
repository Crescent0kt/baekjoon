from collections import deque
N = int(input())

graph = [[] for _ in range(N+1)]

#순서쌍을 만들어줌(그래프)
for _ in range(int(input())):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

Q = deque()

visited[1] = True
Q.append(1)
count = 0

while len(Q) != 0:
    x = Q.popleft()
    count += 1

    for i in graph[x]:
        if visited[i] == False:
            visited[i] = True
            Q.append(i)

print(count - 1)