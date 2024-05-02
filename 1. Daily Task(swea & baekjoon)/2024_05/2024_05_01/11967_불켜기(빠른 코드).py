import sys
input = sys.stdin.readline

# 이동 방향을 나타내는 리스트
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 1  # 방문한 방의 초기값

# 스위치를 누르는 함수
def switch(r, c):
    global cnt

    for r, c in arr[r][c]:  # 스위치를 누르면서 연결된 방을 탐색
        if on[r][c]:  # 아직 불이 켜지지 않았다면
            on[r][c] = False  # 불을 켭니다.
            cnt += 1  # 방문한 방의 수를 증가시킵니다.
            for i in range(4):  # 상하좌우 방향을 탐색합니다.
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:  # 이미 방문한 곳이라면
                    queue.append((r, c))  # 큐에 추가합니다.
                    visit[r][c] = False  # 방문 표시를 합니다.
                    break



N, M = map(int, input().split())  # N: 가로, 세로 M: 스위치 개수

visit = [[True] * N for _ in range(N)]  # 방문 여부를 나타내는 배열
on = [[True] * N for _ in range(N)]  # 불이 켜져있는지를 나타내는 배열

arr = [[[] for _ in range(N)] for _ in range(N)]  # 스위치 정보를 저장할 배열

# 스위치 정보 입력 받기
for i in range(M):
    r, c, x, y = map(int, input().split())
    arr[r - 1][c - 1].append((x - 1, y - 1))  # 스위치를 누르면 연결된 방의 정보를 저장합니다.

queue = [(0, 0)]  # 시작점을 큐에 추가합니다.
visit[0][0] = False  # 시작점을 방문했음으로 표시합니다.
on[0][0] = False  # 시작점의 스위치를 켭니다.



while queue:
    r, c = queue.pop(0)  # 큐에서 방을 하나씩 꺼내어 처리합니다.
    switch(r, c)  # 스위치를 누릅니다.
    for i in range(4):  # 상하좌우 방향을 탐색합니다.
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] and not on[nr][nc]:  # 방문한 적도 없고, 불이 켜져있는 곳이라면
            queue.append((nr, nc))  # 큐에 추가합니다.
            visit[nr][nc] = False  # 방문 여부를 표시합니다.

print(cnt)  # 결과 출력