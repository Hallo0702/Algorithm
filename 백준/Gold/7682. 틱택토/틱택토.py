def check_row(arr,w):
    cnt = 0
    for i in range(3):
        if arr[3*i] == arr[3*i+1] and arr[3*i+1] == arr[3*i+2] and arr[3*i] == w:
            cnt += 1

    return cnt


def check_col(arr,w):
    cnt = 0
    for i in range(3):
        if arr[i] == arr[i+3] and arr[i+3] == arr[i+6] and arr[i] == w:
            cnt += 1

    return cnt


def check_d(arr,w):
    cnt = 0
    if arr[0] == arr[4] and arr[4] == arr[8] and arr[4] == w:
        cnt += 1
    if arr[2] == arr[4] and arr[6] == arr[4] and arr[4] == w:
        cnt += 1

    return cnt


def check_cnt(arr):
    cnt_x = arr.count("X")
    cnt_o = arr.count("O")

    if cnt_o > cnt_x or cnt_x > cnt_o + 1:
        return 0
    elif cnt_o == cnt_x:
        return 1
    else:
        return 2


while 1:
    ST = input()
    if ST == "end":
        break

    case = check_cnt(ST)
    if case == 0: #개수가 안맞으므로 무조건 불가능한 경우
        print("invalid")
    elif case == 1: # O와 X의 개수가 같으므로 마지막에 O가 놓으면서 끝나는 경우여야만 함 ( X는 끝나면 안되고 O는 끝나야 함)
        pos_x = check_row(ST,"X") + check_col(ST,"X") + check_d(ST,"X")
        if pos_x > 0:
            print("invalid")
        else:
            pos_o = check_row(ST,"O") + check_col(ST,"O") + check_d(ST,"O")
            if pos_o == 1:
                print("valid")
            else:
                print("invalid")
    else: # X가 O보다 1개 많은 상황으로 X가 놓으면서 끝나거나 꽉차서 끝나야함, O는 끝나면 안됨.
        pos_o = check_row(ST, "O") + check_col(ST, "O") + check_d(ST, "O")
        if pos_o > 0:
            print("invalid")
        else:
            cnt_dot = ST.count(".")
            if cnt_dot == 0:
                print("valid")
            else:
                pos_x = check_row(ST,"X") + check_col(ST,"X") + check_d(ST,"X")
                if pos_x == 1:
                    print("valid")
                else:
                    print("invalid")

