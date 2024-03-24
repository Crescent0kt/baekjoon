from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    # 그래프 생성 및 역방향으로 정렬하여 스택에서 뽑을 때 알파벳 순으로 뽑히게 함
    for start, end in sorted(tickets, reverse=True):
        graph[start].append(end)
    
    stack = ["ICN"]  # 시작점
    path = []  # 방문 경로
    
    while stack:
        top = stack[-1]  # 현재 공항
        # 현재 공항에서 갈 수 있는 공항이 있으면 스택에 추가
        if graph[top]:
            stack.append(graph[top].pop())
        else:  # 더 이상 갈 수 있는 공항이 없으면 경로에 추가
            path.append(stack.pop())
    
    # 스택에서 뽑힌 순서가 역순이므로 뒤집어줌
    return path[::-1]
