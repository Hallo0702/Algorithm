import sys
sys.setrecursionlimit(10**6)
nodes = []
while True:
    try:
        number = int(input())
        nodes.append(number)
    except:
        break

def postorder(start, end):
    if start > end:
        return
    
    mid = end + 1

    for i in range(start+1,end+1):
        if nodes[start] < nodes[i]:
            mid = i
            break
    
    postorder(start+1,mid-1)
    postorder(mid,end)
    print(nodes[start])

postorder(0,len(nodes)-1)