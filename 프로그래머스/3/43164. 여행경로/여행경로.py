from collections import defaultdict

def solution(tickets):
    answer = []
    dic = defaultdict(list)
    for a,b in sorted(tickets,reverse = True):
        dic[a].append(b)
    
    stack = ["ICN"]
    while stack:
        a = stack[-1]
        if dic[a]:
            stack.append(dic[a].pop())
        else: 
            answer.append(stack.pop())
    return answer[::-1]