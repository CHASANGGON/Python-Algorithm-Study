# # # # 풍선팡2 D2
# # # T = int(input())
# # # for test_case in range(1,T+1):
# # #     N, M = map(int,input().split())

# # #     balloons = [list(map(int,input().split())) for _ in range(N)]
# # #     di = [0,0,1,-1]
# # #     dj = [1,-1,0,0]

# # #     max_total = 0
# # #     for i in range(N):
# # #         for j in range(M):
# # #             total = balloons[i][j]
# # #             for k in range(4):
# # #                 if 0 <= i + di[k] <= N-1 and 0 <= j + dj[k] <= M-1:
# # #                     total += balloons[i+di[k]][j+dj[k]]
# # #             max_total = max(max_total, total)
# # #     print(f'#{test_case} {max_total}')



# # # # 파리 퇴치 D2
# # # T = int(input())
# # # for test_case in range(1,T+1):
# # #     N, M = map(int,input().split())

# # #     bugs = [list(map(int,input().split())) for _ in range(N)]
# # #     di, dj = [], []
# # #     for i in range(M):
# # #         for j in range(M):
# # #             di.append(i)
# # #             dj.append(j)

# # #     max_kill = 0
# # #     for i in range(N-M+1):
# # #         for j in range(N-M+1):
# # #             kill = 0
# # #             for k in range(M**2):
# # #                 kill += bugs[i+di[k]][j+dj[k]]
# # #             max_kill = max(max_kill, kill)
# # #     print(f'#{test_case} {max_kill}')



# # # 1979. 어디에 단어가 들어갈 수 있을까
# # # 문자열로 풀기
# # import copy
# # T = int(input())
# # for test_case in range(1,T+1):
# #     N, K = map(int,input().split())

# #     puzzle = [list(map(int,input().split())) for _ in range(N)]
# #     transpose_puzzle = copy.deepcopy(puzzle)

# #     # 전치 행렬
# #     for i in range(N):
# #         for j in range(N):
# #             if i > j:
# #                 transpose_puzzle[i][j],transpose_puzzle[j][i] = transpose_puzzle[j][i],transpose_puzzle[i][j]
    
# #     # 행렬 합치기
# #     for i in range(N):
# #         puzzle.append(transpose_puzzle[i])

# #     # str 타입 변환, 양끝에 '0' 추가
# #     for i in range(2*N):
# #         str_puzzle = '0'
# #         for j in range(N):
# #             str_puzzle += str(puzzle[i][j])
# #         str_puzzle += '0'
# #         puzzle[i] = str_puzzle
    
# #     # 찾기, 매번 찾고자 하는 길이만큼 이어붙여서 찾고자 하는 대상과 비교
# #     total = 0    
# #     i_want_find_this = '0' + '1'*K + '0'
# #     for i in range(2*N):
# #         for j in range(N-K+1):
# #             compare_this = ''
# #             for k in range(K+2):
# #                 compare_this += puzzle[i][j+k]    
# #             if compare_this == i_want_find_this:
# #                 total += 1

# #     print(f'#{test_case} {total}')



# # 1979. 어디에 단어가 들어갈 수 있을까
# # # 숫자로 풀기
# # import copy
# # T = int(input())
# # for test_case in range(1,T+1):
# #     N, K = map(int,input().split())

# #     puzzle = [list(map(int,input().split())) for _ in range(N)]
# #     transpose_puzzle = copy.deepcopy(puzzle)

# #     # 전치 행렬
# #     for i in range(N):
# #         for j in range(N):
# #             if i > j:
# #                 transpose_puzzle[i][j],transpose_puzzle[j][i] = transpose_puzzle[j][i],transpose_puzzle[i][j]
    
# #     total = 0
# #     for i in range(N):
# #         cnt = 0
# #         for j in range(N):
# #             if puzzle[i][j] == 1:
# #                 cnt += 1
# #             if puzzle[i][j] == 0 or j == N-1:
# #                 if cnt == K:
# #                     total += 1
# #                 cnt = 0

# #     for i in range(N):
# #         cnt = 0
# #         for j in range(N):
# #             if transpose_puzzle[i][j] == 1:
# #                 cnt += 1
# #             if transpose_puzzle[i][j] == 0 or j == N-1:
# #                 if cnt == K:
# #                     total += 1
# #                 cnt = 0

# #     print(f'#{test_case} {total}')



# # 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기 D2
# T = int(input())

# for test_case in range(1,T+1):
#     grid = [[0]*10 for i in range(10)]
    
#     N = int(input())

#     total = 0
#     for i in range(N):
#         x1, y1, x2, y2, color = map(int,input().split())

#         for x in range(x1,x2+1):
#             for y in range(y1,y2+1):
#                 if grid[x][y] == 0: # 아무것도 없으면, 색칠
#                     grid[x][y] = color
#                 elif grid[x][y] | color == 3: # 색이 있으면 purple 인지 판단
#                     grid[x][y] = 3
#                     total += 1
    
#     print(f'#{test_case} {total}')



# 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합 D3
T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    math_set = list(range(1,13))
    n = len(math_set)
    total = 0

    for i in range(1<<n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(math_set[ j])
        if len(subset) == N and sum(subset) == K:
            total += 1

    print(f'#{test_case} {total}')