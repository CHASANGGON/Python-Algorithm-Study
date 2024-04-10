import sys
input = sys.stdin.readline

# 입력
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 찾기
for i in range(R):
    if arr[i][0] == -1:
        purifier1 = i
        purifier2 = i+1
        break

# T초 동안 실행
for _ in range(T):
# 1. 미세먼지 확산
#   2중 for문 -> 공기청정기x or 인덱스 초과x -> 근처로 확산
    diffusion_arr = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0: # 미세먼지가 있으면
                cnt = 0
                diffusion = arr[i][j] // 5
                for di, dj in (1,0), (-1,0), (0,1), (0,-1):
                    ni = i + di
                    nj = j + dj
                    # 배열을 벗어나지 않고, 공기청정기가 아니라면
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1: 
                        diffusion_arr[ni][nj].append(diffusion) # 확산
                        cnt += 1
                diffusion_arr[i][j].append(arr[i][j] - diffusion * cnt)
            # elif arr[i][j] > 0:
            #     diffusion_arr[i][j].append(arr[i][j])
    
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                continue
            arr[i][j] = sum(diffusion_arr[i][j])
    
    # print('휴')
    # 2. 공기청정기 바람 이동 -> 소멸
    #   for문 4개
    
    # 위쪽 공기청정기 작동
    for i in range(purifier1-1,0,-1): # ↓ 방향 이동
        arr[i][0] = arr[i-1][0]
    
    for j in range(C-1): # ← 방향 이동
        arr[0][j] = arr[0][j+1]
    
    for i in range(purifier1): # ↑ 방향 이동
        arr[i][C-1] = arr[i+1][C-1]
        
    for j in range(C-1,1,-1): # → 방향 이동
        arr[purifier1][j] = arr[purifier1][j-1]
    arr[purifier1][1] = 0
    
    
    # 아래쪽 공기청정기 작동
    for i in range(purifier2+1,R-1): # ↑ 방향 이동
        arr[i][0] = arr[i+1][0]
    
    for j in range(C-1): # ← 방향 이동
        arr[R-1][j] = arr[R-1][j+1]
    
    for i in range(R-1,purifier2,-1): # ↓ 방향 이동
        arr[i][C-1] = arr[i-1][C-1]
        
    for j in range(C-1,1,-1): # → 방향 이동
        arr[purifier2][j] = arr[purifier2][j-1]
    arr[purifier2][1] = 0
    
ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            ans += arr[i][j]
            
print(ans)