import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
seg_tree = [0] * (4*N)


def make_seg(idx, s, e):

    if s == e:
        seg_tree[idx] = (arr[s],arr[s])
        return seg_tree[idx]

    mid = (s + e) // 2

    left = make_seg(idx * 2,s, mid)
    right = make_seg(idx * 2 + 1,mid+1,e)

    seg_tree[idx] = (min(left[0],right[0]),max(left[1],right[1]))
    return seg_tree[idx]


def find_m(s, e, idx, a, b):
    if e < a or b < s:
        return (1000000000,0)

    if a <= s and e <= b:
        return seg_tree[idx]

    mid = (s + e) // 2

    left = find_m(s, mid, idx * 2, a, b)
    right = find_m(mid+1, e, idx * 2 + 1, a, b)

    return (min(left[0],right[0]),max(left[1],right[1]))


make_seg(1, 0, N-1)

for i in range(M):
    a, b = map(int, input().split())
    answer = find_m(0, N-1, 1, a-1, b-1)
    print(answer[0],answer[1])