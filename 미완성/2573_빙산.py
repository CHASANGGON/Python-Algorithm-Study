from collections import deque
import sys
import copy

# 인덱스 검사


def in_range(ni, nj):
    return 0 <= ni < N and 0 <= nj < M

#  빙산 시작 위치 탐색
def find_iceberg():
    global si, sj
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                si, sj = i, j
                return True
    return False


input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

day = 0
si, sj = 0, 0
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 빙산이 존재하는 동안 실행
# 빙산이 녹은 값을 저장할 배열 : melt_arr
# 한 번 탐색을 위한 배열 : visited
# melt_arr에서 빙산이 존재할 때 arr의 값과 비교해서 변화가 없다면 한 덩어리!!
while find_iceberg():
    melt_arr = [[0]*M for _ in range(N)]
    day += 1
    visited = [[False]*M for _ in range(N)]

    dq = deque()
    dq.append([si, sj])

    while dq:
        i, j = dq.popleft()

        # 방문 체크
        visited[i][j] = True
        cnt = 0

        # 네 방향 탐색
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            # 인덱스 검사
            if in_range(ni, nj):

                # 값이 있고, 방문하지 않았다면(1)
                if arr[ni][nj] and not visited[ni][nj]:
                    # 탐색할 대상에 추가
                    dq.append([ni, nj])

                # 값이 없다면 바닷물 -> cnt += 1
                elif arr[ni][nj] == 0:
                    cnt += 1

        melt_arr[i][j] = cnt
    print(melt_arr)
    print(arr)
    break

