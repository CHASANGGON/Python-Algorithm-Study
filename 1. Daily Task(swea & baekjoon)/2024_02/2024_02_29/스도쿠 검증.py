def horizontal_inspection():
    for i in range(9):
        cnt_lst = [0]*10
        for j in range(9):
            cnt_lst[arr[i][j]] += 1
        if 2 in cnt_lst:
            return False
    return True
        
def vertical_inspection():
    for i in range(9):
        cnt_lst = [0]*10
        for j in range(9):
            cnt_lst[arr[j][i]] += 1
        if 2 in cnt_lst:
            return False
    return True
        
def square_inspection():
    for i in range(3):
        for j in range(3):
            cnt_lst = [0]*10
            for ii in range(3):
                for jj in range(3):
                    cnt_lst[arr[3*i+ii][3*j+jj]] += 1
            if 2 in cnt_lst:
                return False
    return True

t = int(input())

for tc in range(1,t+1):
    arr = [list(map(int,input().split())) for _ in range(9)]

    if horizontal_inspection() and vertical_inspection() and square_inspection():
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')