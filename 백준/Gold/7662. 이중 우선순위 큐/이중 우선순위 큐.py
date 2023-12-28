from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def isEmpty(num_count):
    for cnt in num_count:
        if cnt > 0:
            return False
    return True


def insert(number):

    if num_count[number] > 0:
        num_count[number] += 1
        return

    else:
        num_count[number] += 1
        heapq.heappush(max_heap,-number)
        heapq.heappush(min_heap,number)
        return


def delete(tp):

    if isEmpty(num_count.values()):
       return

    if tp == '-1':

        while min_heap[0] not in num_count or num_count[min_heap[0]] < 1:
            temp = heapq.heappop(min_heap)
            if temp in num_count:
                del(num_count[temp])
        num_count[min_heap[0]] -= 1

    elif tp == '1':

        while -max_heap[0] not in num_count or num_count[-max_heap[0]] < 1:
            temp = -heapq.heappop(max_heap)
            if temp in num_count:
                del(num_count[temp])
        num_count[-max_heap[0]] -= 1

T = int(input())

for t in range(T):
    K = int(input())

    max_heap = []
    min_heap = []
    num_count = defaultdict(int)

    for k in range(K):
        order, num = input().split()
        if order == 'I':
            insert(int(num))
        elif order == 'D':
            delete(num)

    if isEmpty(num_count.values()):
        print("EMPTY")
    else:
        while min_heap[0] not in num_count or num_count[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        while -max_heap[0] not in num_count or num_count[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        print(-max_heap[0],min_heap[0])

