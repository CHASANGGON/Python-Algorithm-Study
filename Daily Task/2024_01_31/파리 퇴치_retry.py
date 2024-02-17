# # 풍선팡2 D2
# T = int(input())
# for test_case in range(1,T+1):
#     N, M = map(int,input().split())

#     balloons = [list(map(int,input().split())) for _ in range(N)]
#     di = [0,0,1,-1]
#     dj = [1,-1,0,0]

#     max_total = 0
#     for i in range(N):
#         for j in range(M):
#             total = balloons[i][j]
#             for k in range(4):
#                 if 0 <= i + di[k] <= N-1 and 0 <= j + dj[k] <= M-1:
#                     total += balloons[i+di[k]][j+dj[k]]
#             max_total = max(max_total, total)
#     print(f'#{test_case} {max_total}')



# 파리 퇴치 D2
T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())

    bugs = [list(map(int,input().split())) for _ in range(N)]
    di, dj = [], []
    for i in range(M):
        for j in range(M):
            di.append(i)
            dj.append(j)

    max_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for k in range(M**2):
                kill += bugs[i+di[k]][j+dj[k]]
            max_kill = max(max_kill, kill)
    print(f'#{test_case} {max_kill}')