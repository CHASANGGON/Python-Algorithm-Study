# 3차원 배열을 만든다!!
# 3차원에서 벽을 하나 부쉈으면 -> 벽을 부순 2차원으로 이동
# 벽을 아직 안 부쉈다면 -> 부수지 않은 2차원에서 계속 진행

from collections import deque
import copy
import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())

a = [list(map(int, input().rstrip())) for _ in range(n)]
b = copy.deepcopy(a) # 3차원 배열 만들기 위해 b 생성
arr = [] # 탐색에 사용할 3차원 배열
arr.append(a) 
arr.append(b)
        

def bfs():
    dq = deque()
    dq.append([0,0,0])
    arr[0][0][0] = 1 # 방문 기록을 위해 거리를 1로 저장 -> 출력할 때 1을 빼주면 됨
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    
    while dq:
        k,i,j = dq.popleft()
        
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < n and 0 <= nj < m:
                if arr[k][ni][nj] == 0: # 새로 탐색한 곳이 -> 아직 방문한 적 없는 길이라면 
                    arr[k][ni][nj] = arr[k][i][j] + 1 # 최단 거리를 기록
                    dq.append([k,ni,nj]) # 다음 탐색을 위해 dq에 저장
                    
                elif arr[k][ni][nj] == 1 and k == 0 : # 새로 탐색한 곳이 -> 벽이고 & 아직 벽을 부순 적 없다면
                    # 벽을 부순 차원에 <- 최단 거리를 기록
                    arr[1][ni][nj] = arr[k][i][j] + 1
                    dq.append([1,ni,nj])
    
    # 출력
    if arr[0][n-1][m-1] == 0 and arr[1][n-1][m-1] == 0: # 벽을 부쉈든 안 부쉈든 도달 못 했다면
        print(-1)
    elif arr[0][n-1][m-1] and arr[1][n-1][m-1]: # 두 방법 모두 도달 했다면
        print(min(arr[0][n-1][m-1], arr[1][n-1][m-1])) # 최솟값 출력
    elif arr[0][n-1][m-1]: # 한 쪽만 도달했다면 해당값 출력
        print(arr[0][n-1][m-1])
    elif arr[1][n-1][m-1]:
        print(arr[1][n-1][m-1])

bfs()