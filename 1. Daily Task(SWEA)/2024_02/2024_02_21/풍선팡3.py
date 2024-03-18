T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    balloons = [list(map(int,input().split())) for _ in range(n)]
    
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    
    # 3<=N <=20, 1 <= Aij <= 10
    min_pollen = 10 + 4*10*10
    max_pollen = 0
    for i in range(n):
        for j in range(n):
            pollen = balloons[i][j]
            length = pollen
            for k in range(4):
                for l in range(1,length+1):
                    if 0 <= i+di[k]*l < n and 0 <= j+dj[k]*l < n:
                        pollen += balloons[i+di[k]*l][j+dj[k]*l]
                    else: # 해당 방향 탐색 종료
                        break # 다른 방향으로 탐색
            
            # 탐색 끝 -> 값 갱신
            if pollen > max_pollen:
                max_pollen = pollen
            if pollen < min_pollen:
                min_pollen = pollen
    
    print(f'#{test_case} {max_pollen-min_pollen}')