# 문자로 풀기
T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    
    # 가로
    for i in range(N):
        length = 0
        for j in range(N):
            if puzzle[i][j] == 0:
                if length == K:
                    cnt += 1    
                length = 0
                
            elif puzzle[i][j] == 1:
                length += 1
                if length == K and j == N-1 :
                    cnt += 1
            
                
    # 세로
    for i in range(N):
        length = 0
        for j in range(N):
            if puzzle[j][i] == 0:
                if length == K:
                    cnt += 1    
                length = 0
                
            elif puzzle[j][i] == 1:
                length += 1
                if length == K and j == N-1 :
                    cnt += 1
                    
    print(f'#{test_case} {cnt}')