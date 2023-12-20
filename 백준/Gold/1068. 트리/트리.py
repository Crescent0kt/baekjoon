import sys
from collections import defaultdict

N = int(sys.stdin.readline())
d = defaultdict(list)
answer = 0

node_list = list(map(int,sys.stdin.readline().split()))
root = -1
for i,parent in enumerate(node_list):
    if parent == -1:
        root = i
    d[parent].append(i)
cut_node = int(sys.stdin.readline())
if cut_node == root:
    print(0)
    exit()

stack = [root]

while stack:
    node = stack.pop()
    next_nodes = d[node]
    if cut_node in next_nodes:
        next_nodes.remove(cut_node)
    if len(next_nodes) == 0:
        answer += 1
        continue
    else:
        for next_node in next_nodes:
            stack.append(next_node)
print(answer)
