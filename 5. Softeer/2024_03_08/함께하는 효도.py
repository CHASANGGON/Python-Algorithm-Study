def m_P(i):
    if i == M:
        m_order.append(p_lst[:])
    else:
        for j in range(i,M):
            p_lst[i], p_lst[j] = p_lst[j], p_lst[i]
            m_P(i+1)
            p_lst[i], p_lst[j] = p_lst[j], p_lst[i]

def in_range(ni,nj):
    return 0 <= ni < N and 0 <= nj < N

# 좌표, 경로, 수확량, 탐색 깊이
def P(i, j, S, D):
    global max_path
    global max_S
    # 기저 조건
    if D == 3:
        if S > max_S:
            max_S = S # 최대 수확량 갱신
            max_path = copy.deepcopy(path)  # 최대 수확량 경로 갱신
            
    else:
        # 방문 체크
        V[i][j] = 0
        
        # 네 방향 완전 탐색 -> 중복 허용 순열
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 인덱스 검사
            if in_range(ni,nj) and V[ni][nj]:
                path.append([ni,nj]) # 경로 추가 후 재귀 호출
                P(ni, nj, S+arr_copy[ni][nj], D+1)
                path.pop() # 복구
        # 방문 복구
        V[i][j] = 1

import copy
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

m_lst = []
for _ in range(M):
    m_lst.append(list(map(int,input().split())))
    
# m명의 친구들 탐색 순서 순열 생성
cnt = 0
m_order = []
p_lst = list(range(M))
m_P(0)


# 탐색에 필요한 것들
V = [[1]*N for _ in range(N)]
di = [1,-1,0,0]
dj = [0,0,1,-1]
result = 0
for mo in m_order:
    arr_copy = copy.deepcopy(arr)
    s = 0
    for mm in mo:
        i = m_lst[mm][0] - 1
        j = m_lst[mm][1] - 1         
        max_S = 0
        path = [[i,j]]
        max_path = []
        # 좌표, 경로, 수확량, 탐색 깊이
        P(i, j, arr_copy[i][j], 0)
        for i, j in max_path:
            s += arr_copy[i][j]
            arr_copy[i][j] = 0
    result = max(result,s)
print(result)