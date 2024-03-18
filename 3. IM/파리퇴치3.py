T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    bug = [list(map(int,input().split())) for _ in range(N)]
    
    
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    di_dng = [1,1,-1,-1]
    dj_dng = [1,-1,1,-1]
    max_kill = 0
    for i in range(N): # 좌표 변경
        for j in range(N):
            kill = bug[i][j] # 상하좌우
            kill_dng = bug[i][j] # 대각선
            for k in range(4): # 방향 변경
                for l in range(1,M): # 길이 변경
                    if 0 <= i+di[k]*l < N and 0 <= j+dj[k]*l < N:
                        kill += bug[i+di[k]*l][j+dj[k]*l]
                    if 0 <= i+di_dng[k]*l < N and 0 <= j+dj_dng[k]*l < N:
                        kill_dng += bug[i+di_dng[k]*l][j+dj_dng[k]*l]
            if max_kill < kill:
                max_kill = kill
            if max_kill < kill_dng:
                max_kill = kill_dng
                
    print(f'#{tc} {max_kill}')                         