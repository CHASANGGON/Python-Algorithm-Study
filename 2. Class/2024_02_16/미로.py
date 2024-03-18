# 테스트케이스 수 T
T = int(input())

for tc in range(1, T + 1):
    # 입력
    # 미로의 한변의 길이 N
    N = int(input())
    # 미로의 정보 NxN maze
    maze = [list(map(int, input())) for _ in range(N)]

    # "13101
    # 10101
    # 10101
    # 10101
    # 10021"
    # 로직
    # DFS 알고리즘으로 하여서
    # 시작점2 에서부터 도착점3으로 갈 수 있는지 없는지
    # is_success = False  # 도착지점에 도달한 경우 True...
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]


    # # 방문체크를 할 NxN 배열...
    # visited = [[False] * N for _ in range(N)]
    #
    #
    # def dfs(x, y):  # (x, y) 좌표로부터 DFS 탐색 계속 수행...
    #     # 기저조건 : 도착지 (ex, ey)도달 했는가...!
    #     if x == ex and y == ey:
    #         is_success = True
    #         return
    #     # 상하좌우...! (재귀호출)
    #     for d in range(4):
    #         # 다음 이동할 좌표 (nx, ny)
    #         nx = x + dx[d]
    #         ny = y + dy[d]
    #         # 해당 좌표가 갈 수 있는 좌표인지... (벽일 때에 갈 수 없음)
    #         if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1:
    #             if visited[nx][ny] == False:
    #                 visited[nx][ny] = True
    #                 dfs(nx, ny)
    #
    #
    # # 시작지점과 도착지점을 가져온다..!
    # for i in range(N):
    #     for j in range(N):
    #         if maze[i][j] == 2:  # 시작점
    #             sx, sy = (i, j)
    #         elif maze[i][j] == 3:  # 도착지점
    #             ex, ey = (i, j)
    #
    # # 시작점에서부터 모든 경로를 탐색...!
    # dfs(sx, sy)
    # # # 출력
    # # if is_success:
    # #     print(f"#{tc} 1")
    # # else:
    # #     print(f"#{tc} 0")
    # if visited[ex][ey]:
    #     print(f"#{tc} 1")
    # else:
    #     print(f"#{tc} 0")

    # def dfs(x, y):  # (x, y) 좌표로부터 DFS 탐색 계속 수행...
    #     # 기저조건(필수는 아님) : 도착지 (ex, ey)도달 했는가...!
    #     if x == ex and y == ey:
    #         return
    #     # 상하좌우...! (재귀호출)
    #     for d in range(4):
    #         # 다음 이동할 좌표 (nx, ny)
    #         nx = x + dx[d]
    #         ny = y + dy[d]
    #         # 해당 좌표가 갈 수 있는 좌표인지... (벽일 때에 갈 수 없음)
    #         if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1:
    #             maze[nx][ny] = 1
    #             dfs(nx, ny)
    #
    #
    # # 시작지점과 도착지점을 가져온다..!
    # for i in range(N):
    #     for j in range(N):
    #         if maze[i][j] == 2:  # 시작점
    #             sx, sy = (i, j)
    #         elif maze[i][j] == 3:  # 도착지점
    #             ex, ey = (i, j)
    #
    # # 시작점에서부터 모든 경로를 탐색...!
    # dfs(sx, sy)
    # # # 출력
    # if maze[ex][ey] == 1:  # 해당 도착지점이 벽이 되어 있다면 도달...!
    #     print(f"#{tc} 1")
    # else:
    #     print(f'#{tc} 0')

    def solution(maze, N):
        # 초기값 설정...
        visited = [[False] * N for _ in range(N)]
        is_success = False  # 실패/성공 여부...

        # 재귀함수 정의...
        def dfs(x, y):  # (x, y) 좌표로부터 DFS 탐색 계속 수행...
            nonlocal is_success
            # 기저조건(필수는 아님) : 도착지 (ex, ey)도달 했는가...!
            if x == ex and y == ey:
                is_success = True
                return
            # 상하좌우...! (재귀호출)
            for d in range(4):
                # 다음 이동할 좌표 (nx, ny)
                nx = x + dx[d]
                ny = y + dy[d]
                # 해당 좌표가 갈 수 있는 좌표인지... (벽일 때에 갈 수 없음)
                if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1:
                    maze[nx][ny] = 1
                    dfs(nx, ny)
                    if is_success:
                        return

        # 시작지점과 도착지점을 가져온다..!
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:  # 시작점
                    sx, sy = (i, j)
                elif maze[i][j] == 3:  # 도착지점
                    ex, ey = (i, j)
        # 재귀함수 실행...
        dfs(sx, sy)
        return is_success


    result = solution(maze, N)
    # 출력
    if result:  # 도착지점에 도달했다면...
        print(f"#{tc} 1")
    else:
        print(f'#{tc} 0')