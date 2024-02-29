def out_of_range(ni,nj):
    return 0 <= ni < n and 0 <= nj < n

t = int(input())

for tc in range(1,t+1):

    # 입력
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    # 상하좌우 델타
    di_1 = [1,-1,0,0]
    dj_1 = [0,0,1,-1]

    # 대각선 델타
    di_2 = [1,1,-1,-1]
    dj_2 = [1,-1,1,-1]

    # 최댓값 갱신용 변수
    max_kill = 0

    # 모든 좌표 탐색
    for i in range(n):
        for j in range(n):
            
            # 변수 생성
            kill_2, kill_1 = arr[i][j], arr[i][j]
            
            # 상하좌우 탐색
            for k in range(4):
                for l in range(1,m):
                    ni = i + di_1[k]*l
                    nj = j + dj_1[k]*l
                    
                    # 인덱스 검사
                    if out_of_range(ni,nj):
                        kill_1 += arr[ni][nj]
                    else:
                        break

            # 대각선 탐색
            for k in range(4):
                for l in range(1,m):
                    ni = i + di_2[k]*l
                    nj = j + dj_2[k]*l
                    
                    # 인덱스 검사
                    if out_of_range(ni,nj):
                        kill_2 += arr[ni][nj]
                    else:
                        break
            
            max_kill = max(max_kill, kill_1, kill_2)

    print(f'#{tc} {max_kill}')