# # 5789. 현주의 상자 바꾸기 D3
# T = int(input())

# for test_case in range(1,T+1):
#     N, Q = map(int,input().split())

#     boxes = [0]*N

#     for i in range(1,Q+1):
#         L, R = map(int,input().split())
#         for j in range(L-1,R):
#             boxes[j] = i
    
#     print(f'#{test_case} ',end='')
#     print(*boxes)



# 1210. [S/W 문제해결 기본] 2일차 - Ladder1 D4
T = 10
for test_case in range(1,T+1):
    input()
    ladder = [list(map(int,input().split())) for _ in range(100)]
    

    i = 99
    j = ladder[99].index(2)

    while i != 0:
        if 0 <= j+1 <= 99 and ladder[i][j+1] == 1:
                while 0 <= j+1 <= 99 and ladder[i][j+1] == 1:
                     j += 1
                i -= 1
        elif 0 <= j-1 <= 99 and ladder[i][j-1] == 1:
                while 0 <= j-1 <= 99 and ladder[i][j-1] == 1:
                     j -= 1
                i -= 1
        else:
            i -= 1
    
    print(F'#{test_case} {j}')
