# 1979. 어디에 단어가 들어갈 수 있을까
# 숫자로 풀기
import copy
T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())

    # 입력
    puzzle = [list(map(int,input().split())) for _ in range(N)] 
    
    # 전체 개수를 카운트할 변수
    total = 0
    
    # 가로 방향 탐색
    for i in range(N):
        cnt = 0
        for j in range(N):
            # 1일 때는 cnt 값을 증가
            if puzzle[i][j] == 1:
                cnt += 1
            # 0이거나 인덱스의 끝에서 cnt 값을 검사
            if puzzle[i][j] == 0 or j == N-1:
                # K와 일치하면 total +1
                if cnt == K:
                    total += 1
                # cnt 초기화
                cnt = 0

    # 세로 방향 탐색
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K:
                    total += 1
                cnt = 0

    print(f'#{test_case} {total}')