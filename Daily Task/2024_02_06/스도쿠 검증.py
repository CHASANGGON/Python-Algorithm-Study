T = int(input())

for test_case in range(1,T+1):
    sudoku = [list(map(int,input().split())) for i in range(9)]
    result = 1

    # 가로 검증
    for i in range(9):
        cnt_row = [0]*10   # index를 바로 사용하기 위해 10개 선언
        for j in range(9): # -> index0은 사용 x    
            cnt_row[sudoku[i][j]] += 1
        if 2 in cnt_row:
            result = 0

    # 세로 검증
    for i in range(9):
        cnt_col = [0]*10 # index 0은 사용 x    
        for j in range(9):
            cnt_col[sudoku[j][i]] += 1
        if 2 in cnt_col:
            result = 0

    # 사각 검증
    for a in range(3):
        for b in range(3):
            cnt_rect = [0]*10
            for i in range(3):
                for j in range(3):
                    cnt_rect[sudoku[3*a+i][3*b+j]] += 1
            if 2 in cnt_rect:
                result = 0

    print(f'#{test_case} {result}')