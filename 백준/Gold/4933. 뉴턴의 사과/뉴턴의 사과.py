import sys
from collections import deque
input = sys.stdin.readline


def EqualTree(tree1,tree2,s1,s2):

    if s1 != s2:
        return 'false'

    q = deque()
    q.append(s1)

    while q:
        node = q.popleft()
        left = tree1[node]
        right = tree2[node]
        left.sort()
        right.sort()

        if left != right:
            return 'false'

        if left[0] != 'nil':
            q.append(left[0])

        if left[1] != 'nil':
            q.append(left[1])

    return 'true'


T = int(input())
for t in range(T):
    first_tree = list(input().split())
    second_tree = list(input().split())

    first_dict = {}
    second_dict = {}

    stack = []
    for w in first_tree:
        if w == 'end':
            start1 = first_tree[-2]

        elif w == 'nil':
            stack.append('nil')

        else:
            first_dict[w] = []
            first_dict[w].append(stack.pop())
            first_dict[w].append(stack.pop())
            stack.append(w)

    for w in second_tree:
        if w == 'end':
            start2 = second_tree[-2]

        elif w == 'nil':
            stack.append('nil')

        else:
            second_dict[w] = []
            second_dict[w].append(stack.pop())
            second_dict[w].append(stack.pop())
            stack.append(w)

    answer = EqualTree(first_dict,second_dict,start1,start2)

    print(answer)


