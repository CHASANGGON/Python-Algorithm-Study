def in_range(ni,nj): # 인덱스 검사
    return 0 <= ni < N and 0 <= nj < M

def dfs():
    # 스택이 비워질 때까지 = 더 이상 탐색할 곳이 없을 때까지
    while stack:
        i, j = stack.pop()
        arr[i][j] = 0 # 방문 표시
        
        for k in range(4): # 델타 탐색
            
            ni = i + di[k] # 새로운 좌표
            nj = j + dj[k]
            # 인덱스 검사           배추인지 아닌지
            if in_range(ni,nj) and arr[ni][nj]:
                stack.append([ni,nj])
    
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(1,t+1):
    # 가로 세로 배추
    M, N, K = map(int,input().split())
    arr = [[0]*M for _ in range(N)] # 배열 생성
    
    for _ in range(K): # 배추 정보 입력
        j, i = map(int,input().split())
        arr[i][j] = 1
    
    # 탐색에 사용할 델타
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    cnt = 0 # 필요한 지렁이를 카운트할 변수
    
    # 배열을 순회하면서
    for i in range(N):
        for j in range(M):
            # 배추를 만나면 DFS!
            if arr[i][j]:
                cnt += 1 # 지렁이 +1
                stack = [[i,j]] # 현재 좌표를 stack에 담아서 dfs 출발!
                dfs()
    
    print(cnt)