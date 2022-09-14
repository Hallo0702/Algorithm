from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [deque(list(map(int, input().split())))]

#물고기 넣기
def put_fish(board):
    min_num = min(board[0])
    for i in range(N):
        if arr[0][i] == min_num:
            arr[0][i] += 1
    return board


def left_up(board):
    num = board[0].popleft()
    board.append(deque([num]))
    return board


def turn_90(board):
    new_board = [[0 for _ in range(len(board))] for _ in range(len(board[0]))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            new_board[j][len(board)-i-1] = board[i][j]

    return new_board


def sky_fly(board):
    while 1:
        if len(board) > len(board[0]) - len(board[-1]):
            break

        fly_list = []
        r = len(board)
        c = len(board[-1])

        for i in range(r-1,-1,-1):
            q = deque()
            for j in range(c):
                q.append(board[i].popleft())
            fly_list.append(q)


        next_board = [board[0]]
        fly_board = turn_90(fly_list)
        for i in range(len(fly_board)-1,-1,-1):
            next_board.append(deque(fly_board[i]))

        board = deepcopy(next_board)

    return board


def d_mix(board):
    tmp_board = [[0 for _ in range(len(board[k]))] for k in range(len(board))]
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]

                if 0 <= y < len(board) and 0 <= x < len(board[y]):
                    if board[y][x] > board[i][j]:
                        tmp_board[i][j] += (board[y][x] - board[i][j]) // 5
                    else:
                        tmp_board[i][j] -= (board[i][j] - board[y][x]) // 5

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += tmp_board[i][j]

    return board


def sort_board(board):
    new_board = deque()

    for j in range(len(board[-1])):
        for i in range(len(board)):
            new_board.append(board[i][j])

    for j in range(len(board[-1]),len(board[0])):
        new_board.append(board[0][j])

    result = list()
    result.append(new_board)
    return result


def half_reverse(board):
    new_board = [[] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])//2):
            new_board[i].append(board[i].popleft())
    for i in range(len(board)):
        new_board[i].reverse()
    for i in range(len(board)-1,-1,-1):
        board.append(deque(new_board[i]))

    return board

def check(board):
    max_num = max(board[0])
    min_num = min(board[0])
    if max_num - min_num <= K:
        return True
    else:
        return False

turn = 0
while 1:
    turn += 1
    arr = put_fish(arr)
    arr = left_up(arr)
    arr = sky_fly(arr)
    arr = d_mix(arr)
    arr = sort_board(arr)
    arr = half_reverse(arr)
    arr = half_reverse(arr)
    arr = d_mix(arr)
    arr = sort_board(arr)
    flag = check(arr)
    if flag:
        print(turn)
        break