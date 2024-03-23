# 1. 배열을 입력받은 후에 0인 곳을 모두 리스트에 담기
# 2. 매번 검사 및 DFS

def square(i, j, value):
    offset_i = (i // 3) * 3
    offset_j = (j // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[offset_i + i][offset_j + j] == value:
                return False
    return True
    
def horizontal(i, value):
    for j in range(9):
        if sudoku[i][j] == value:
            return False
    return True
    
def vertical(j, value):
    for i in range(9):
        if sudoku[i][j] == value:
            return False
    return True
    
def dfs(depth):
    # 기저 조건 & 출력
    if depth == N:
        for sdk in sudoku:
            print(*sdk)
        exit()

    i = not_exist[depth][0]
    j = not_exist[depth][1]
    for value in range(1,10):
        if square(i, j, value) and horizontal(i, value) and vertical(j, value):
            sudoku[i][j] = value
            dfs(depth+1)
            sudoku[i][j] = 0

import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]

not_exist = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            not_exist.append([i,j])
            
N = len(not_exist) # 기저 조건에 사용할 n       
dfs(0)