import copy
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    arr_1 = [list(map(int,input().split())) for _ in range(N)]
    
    arr_2 = copy.deepcopy(arr_1)
    for i in range(N): # 전치행렬
        for j in range(N):
            if i > j:
                arr_2[i][j], arr_2[j][i] = arr_2[j][i], arr_2[i][j]
    
    count = length = 0
    for i in range(N): 
            length = 0
            for j in range(N):
                if arr_1[i][j]:
                    length += 1
                if arr_1[i][j] == 0 or j == N-1:
                    if length == K:
                        length = 0
                        count += 1
                    length = 0

    for i in range(N):
            length = 0
            for j in range(N):
                if arr_2[i][j]:
                    length += 1
                if arr_2[i][j] == 0 or j == N-1:
                    if length == K:
                         length = 0
                         count += 1 
                    length = 0


    print(f'#{test_case} {count}')