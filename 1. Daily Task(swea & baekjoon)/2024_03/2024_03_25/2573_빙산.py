# 1. 빙산이 있는 곳에서 부터 DFS BFS 암거나 
# 2. 탐색을 하며 주변의 녹아야할 값을 구해서 배열에 저장.
#     이 때 visited를 이용해서 값이 있는데, 방문하지 않은 곳이 있다면 그 곳은 분리된 곳 -> 즉시 탈출
# 3. 빙산이 없으면 일수를 출력

def start():
    global si, sj
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                si, sj = i, j
                return True
    return False

def dfs(si, sj):
    stack = [[si, sj]]
    melted = [[0] * m for _ in range(n)]
    visited = [[1] * m for _ in range(n)]
    while stack:
        i, j = stack.pop()
        cnt = 0 # 인접 바다수 카운트
        
        for k in range(4): # 주위 네 방향 탐색
            ni = i + di[k]
            nj = j + dj[k]
            # 인덱스 검사
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] and visited[ni][nj]: # 빙산이고 방문한 적 없다면
                    visited[ni][nj] = 0 # 방문 처리
                    stack.append([ni,nj])
                elif arr[ni][nj] == 0: # 바다라면 카운트                
                    cnt += 1
        melted[i][j] = cnt # 다 탐색했으면 melted에 저장
    
    # 다 돌았으면 분리된 곳을 체크
    for i in range(n):
        for j in range(m):
            # 빙산은 있는데
            if arr[i][j]: # 방문한 적 없다면 분리된 것!
                if visited[i][j]:
                    return False
                else:
                    arr[i][j] = max(0, arr[i][j] - melted[i][j])
    
    return True
    
import sys
input = sys.stdin.readline

n, m  = map(int,input().split()) # 입력
arr = [list(map(int,input().split())) for _ in range(n)]

di = [1,-1,0,0]
dj = [0,0,1,-1]

day = 0
si, sj = 0, 0
while start(): # 빙산이 있는데
    if dfs(si, sj): # 분리되지 않았다면
        day += 1
    else: # 분리됐으면
        print(day)
        exit()

print(0) # 빙산이 없는데 분리도 안 됐다면 