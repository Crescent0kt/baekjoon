import sys
import collections
"""
#N: 도시 수, M: 도로 수, K: 거리 정보, X: 출발 도시 번호
X에서 정확히 K 거리에 해당하는 도시 번호를 출력하는 문제
"""
N,M,K,X = map(int,sys.stdin.readline().split())

edges = collections.defaultdict(list)

for _ in range(M):
    departure, arrival = map(int, sys.stdin.readline().split())
    edges[departure].append(arrival)

visited = [M+1] * (N+1)
stack = [[X,0]]
visited[X] = 0

while stack:
    node, count = stack.pop()
    if count >K: continue
    next_nodes = edges[node]

    for next_node in next_nodes:
        if visited[next_node]> count+1:
            visited[next_node]= count+1
            stack.append([next_node,count+1])

answer = []
for i,visit_node in enumerate(visited):
    if visit_node == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    for a in answer:
        print(a)