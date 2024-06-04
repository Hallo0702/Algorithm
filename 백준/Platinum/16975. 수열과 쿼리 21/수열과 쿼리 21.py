import sys

input = sys.stdin.readline


def make_seg(node,s, e):
    if s == e:
        seg_tree[node] = A[s-1]
        return

    mid = (s+e)//2
    make_seg(node*2,s,mid)
    make_seg(node*2+1,mid+1,e)


def plus(s, e, left, right, node, value):
    if e < left or s > right:
        return

    if left <= s and e <= right:
        seg_tree[node] += value
        return

    mid = (s+e)//2
    plus(s,mid,left,right,node*2,value)
    plus(mid+1,e,left,right,node*2+1,value)


def cal(node, s, e, idx, value):
    if idx < s or e < idx:
        return 0

    value += seg_tree[node]

    if s == e:
        return value

    mid = (s + e) // 2
    return cal(node*2,s,mid,idx,value) + cal(node*2+1,mid+1,e,idx,value)


N = int(input())
A = list(map(int, input().split()))
seg_tree = [0] * (4*N + 1)
make_seg(1,1,N)
M = int(input())
for _ in range(M):
    Q = list(map(int, input().split()))
    if Q[0] == 1:
        plus(1,N,Q[1],Q[2],1,Q[3])
    else:
        print(cal(1,1,N,Q[1],0))
