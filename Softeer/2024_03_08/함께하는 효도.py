# m명의 친구
# n * n 크기의 격자 모양 나무
# 각 나무마다 가능한 열매 수확량
# 서로 다른 위치에서 출발
# 1초에 1칸씩 상하좌우 인접한 칸 -> dfs
# 최종적으로 모든 열매 수확량의 합을 최대
# 열매를 수확하는데 걸리는 시간은 0초
# 여러 친구가 방문하게 되더라도 열매는 딱 한 번만 수확
# 친구들끼리 이동하는 도중 만나게 되는 것 역시 가능
# m명의 친구들이 3초 동안 최대로 얻을 수 있는 열매 수확량의 총 합

# 인덱스 검사
def in_range(ni,nj):
    return 0 <= ni < N and 0 <= nj < N

# 좌표, visited, 탐색 깊이
def dfs(i, j, V, D):
    # 기저 조건
    if D == 3:
        return arr[i][j]
    
    else:
        # 방문 표시 -> 재탐색 방지
        V[i][j] = 0 
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if in_range(ni,nj) and V[ni][nj]:
                arr[i][j] = max(arr[i][j], dfs(ni,nj,V, D+1)+arr[i][j])
        # 복구
        V[i][j] = 1
        return arr[i][j]


import sys
input = sys.stdin.readline

N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

m_lst = []
for _ in range(M):
    m_lst.append(list(map(int,input().split())))
    
# 탐색에 필요한 것들
V = [[1]*N for _ in range(N)]
di = [1,-1,0,0]
dj = [0,0,1,-1]
s = 0

for i,j in m_lst:
    s += dfs(i, j, V, 0)
    
print(s)