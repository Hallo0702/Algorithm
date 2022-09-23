def dfs(now, root, sheep, wolf):
    global Max
    if nodes[now] == 0:
        sheep += 1
    else:
        wolf += 1
    
    if sheep > Max:
        Max = sheep
    
    if sheep <= wolf:
        return
    
    root = root + graph[now]
    
    if now != 0 and root == []:
        return
    
    l = len(root)
    
    for idx,nextnode in enumerate(root):
        dfs(nextnode,root[0:idx]+root[idx+1:l],sheep,wolf)
        


def solution(info, edges):
    global Max, nodes, graph
    answer = 0
    graph = [[] for _ in range(len(info))]
    
    for up, down in edges:
        graph[up].append(down)
        
    nodes = info
    Max = 0
    dfs(0,[],0,0)
    answer = Max
    return answer