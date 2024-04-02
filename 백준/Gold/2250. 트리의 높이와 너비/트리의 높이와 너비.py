import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
binary_tree = [[-1,-1,-1,1,-1] for _ in range(n+1)] # 부모노드, 왼쪽 자식, 오른쪽 자식, 깊이, 번호
for i in range(n):
    node, l_leaf, r_leaf = map(int, input().split())
    binary_tree[node][1] = l_leaf
    binary_tree[node][2] = r_leaf
    binary_tree[l_leaf][0] = node
    binary_tree[r_leaf][0] = node

root = -1
for i in range(1, n+1):
    if binary_tree[i][0] == -1:
        root = i
        break

visit = [-1 for _ in range(n+1)]


def bfs(node):
    maxdepth = 1
    q = deque()
    q.append(node)
    visit[node] = 1

    while q:
        node = q.popleft()
        l_leaf = binary_tree[node][1]
        r_leaf = binary_tree[node][2]
        if l_leaf != -1 and visit[l_leaf] == -1:
            visit[l_leaf] = 1
            binary_tree[l_leaf][3] = binary_tree[node][3] + 1
            maxdepth = max(maxdepth,binary_tree[l_leaf][3])
            q.append(l_leaf)

        if r_leaf != -1 and visit[r_leaf] == -1:
            visit[r_leaf] = 1
            binary_tree[r_leaf][3] = binary_tree[node][3] + 1
            maxdepth = max(maxdepth, binary_tree[r_leaf][3])
            q.append(r_leaf)

    return maxdepth


global row
row = 0


def inorder(node):
    global row
    if binary_tree[node][1] != -1:
        inorder(binary_tree[node][1])
    row += 1
    binary_tree[node][4] = row
    if binary_tree[node][2] != -1:
        inorder(binary_tree[node][2])



maxdepth = bfs(root)
inorder(root)
order = [[] for _ in range(maxdepth+1)]
answer = [0,0]
for i in range(1,n+1):
    order[binary_tree[i][3]].append(binary_tree[i][4])

for i in range(1,maxdepth+1):
    min_val = min(order[i])
    max_val = max(order[i])
    result = max_val - min_val + 1
    if answer[1] < result:
        answer[1] = result
        answer[0] = i

print(*answer)