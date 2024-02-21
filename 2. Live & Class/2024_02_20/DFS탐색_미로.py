# 테스트케이스 갯수
T = 10
N = 16  # 미로 한변의 길이
for _ in range(1, T + 1):
    # 입력
    # 테스트케이스 번호 tc
    tc = int(input())
    # NxN 이차원 미로 maze
    maze = [list(map(int, input())) for _ in range(N)]

    # 로직 DFS 탐색...
    # 방문체크 N * N 행렬
    visited = [[False] * N for _ in range(N)]
    # 델타탐색 (상하좌우)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]


    def dfs(x, y):
        # 기저조건...
        if maze[x][y] == 3:  # 도착지점
            return
        # 방문체크
        visited[x][y] = True
        # 재귀호출...(상하좌우)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # (nx, ny) 좌표가 범위 바깥을 나가는 경우... 패스!
            #     //         벽인 경우...!
            #     //         이미 방문이 되어 있다면... 패스!
            if nx < 0 or nx >= N or ny < 0 or ny >= N or maze[nx][ny] == 1 or visited[nx][ny]:
                continue
            dfs(nx, ny)


    for i in range(N):
        for j in range(N):
            # (i, j) 좌표가 2의 값을 가지고 있다면 = 시작점
            if maze[i][j] == 2:
                sx, sy = i, j
    dfs(sx, sy)  # 도착지에 도달할 수 있는가...!

    # 도착지점(ex, ey)에 대해서 방문체크가 되어 있다면..? 시작지점과 연결된 경로가 있다!
    for i in range(N):
        for j in range(N):
            # (i, j) 좌표가 2의 값을 가지고 있다면 = 시작점
            if maze[i][j] == 3:
                ex, ey = i, j

    if visited[ex][ey] == True:
        result = 1  # 방문을 할 수 있습니다. (경로가 있어요!)
    else:
        result = 0  # 경로가 없어요 ㅠ

    print(f"#{tc} {result}")