from collections import deque
import sys
import copy

# 값 변화 검사


def change_check(arr, melt_arr):
    for i in range(N):
        for j in range(M):
            # 빙산이 존재하는데, 녹은 값이 0이라면()
            if arr[i][j] and not melt_arr[i][j]:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]

                    # 인덱스 검사
                    if in_range(ni, nj) and arr[ni][nj] == 0:
                        # 두 덩어리 이상으로 분리된 거
                        return False
    return True

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

    # 값 변화 체크
    # 모든 값이 변화가 있으면 True
    # 한 개라도 변화가 없으면 False
    result = change_check(arr, melt_arr)

    # 한 개라도 변화가 없는 경우 -> 두 덩어리 이상으로 분리된 상황 -> day 출력
    if result == False:
        break

    # 아무 일도 일어나지 않았다면 melt값을 반영
    for i in range(N):
        for j in range(M):
            arr[i][j] = max(0, arr[i][j] - melt_arr[i][j])

print(day-1)
