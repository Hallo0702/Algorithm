import sys
input = sys.stdin.readline
sdoku = list(list(map(int, list(input().rstrip()))) for _ in range(9))


def solve(x,y):

    if x == 9:
        for i in range(9):
            print("".join(map(str,sdoku[i])))
        exit()

    if sdoku[x][y] == 0:
        for i in range(1,10):
            if check_row(x,i) and check_col(y,i) and check_box(x//3,y//3,i):
                sdoku[x][y] = i
                if y == 8:
                    solve(x+1,0)
                else:
                    solve(x,y+1)
                sdoku[x][y] = 0
    else:
        if y == 8:
            solve(x+1,0)
        else:
            solve(x,y+1)


def check_row(row,num):
    for i in range(0,9):
        if sdoku[row][i] == num:
            return False
    return True


def check_col(col,num):
    for i in range(0,9):
        if sdoku[i][col] == num:
            return False
    return True


def check_box(row,col,num):
    for i in range(3):
        for j in range(3):
            if sdoku[3*row+i][3*col+j] == num:
                return False
    return True

solve(0,0)