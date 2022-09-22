def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    tmp_board = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for tp, r1, c1, r2, c2, degree in skill:
        if tp == 1:
            tmp_board[r1][c1] += degree * (-1)
            tmp_board[r1][c2+1] += degree
            tmp_board[r2+1][c1] += degree
            tmp_board[r2+1][c2+1] += degree * (-1)
        else:
            tmp_board[r1][c1] += degree
            tmp_board[r1][c2+1] += degree * (-1)
            tmp_board[r2+1][c1] += degree * (-1)
            tmp_board[r2+1][c2+1] += degree
    
    for i in range(n+1):
        for j in range(1,m+1):
            tmp_board[i][j] += tmp_board[i][j-1]
        
    for j in range(m+1):
        for i in range(1,n+1):
            tmp_board[i][j] += tmp_board[i-1][j]
        
    for i in range(n):
        for j in range(m):
            if board[i][j] + tmp_board[i][j] > 0:
                answer += 1
        
        
    
    return answer