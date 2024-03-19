# 테스트케이스 갯수
from collections import deque

T = 10
N = 16  # 미로 한변의 길이
for _ in range(1, T + 1):
    # 입력
    # 테스트케이스 번호 tc
    tc = int(input())
    # NxN 이차원 미로 maze
    maze = [list(map(int, input())) for _ in range(N)]

    # 로직 DFS 탐색...

    # 델타탐색 (상하좌우)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def bfs(x, y):
        # 너비우선탐색을 진행하되
        # 시작지점으로부터 인접되어 있는 노드들을 순차적으로 방문...!
        #                      ㄴ> 큐에다가 넣으면서 방문을 진행하겠다..
        q = deque()
        # 방문체크를 위한 N * N 배열
        visited = [[False] * N for _ in range(N)]
        # 시작지점을 큐에 삽입...
        q.append((x, y))
        visited[x][y] = True
        # 큐가 빌때 까지 순회를 반복...
        while q:
            # 큐에 노드를 하나 꺼내고 (좌표)
            x, y = q.popleft()
            # 해당 (x, y 좌표가 종료지점인 경우 중단...!)
            if maze[x][y] == 3:  # 종료지점이라면...
                return 1
            # 그 큐에 인접되어 있는 좌표들을 다시 큐에 넣어서 진행...
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # (nx, ny) 좌표가 범위 바깥을 나가는 경우... 패스!
                #     //         벽인 경우...!
                #     //         이미 방문이 되어 있다면... 패스!
                if nx < 0 or nx >= N or ny < 0 or ny >= N or maze[nx][ny] == 1 or visited[nx][ny]:
                    continue
                q.append((nx, ny))
                visited[nx][ny] = True
        return 0  # 도착지점에 도달할 수 가 없네요 ㅠ

    for i in range(N):
        for j in range(N):
            # (i, j) 좌표가 2의 값을 가지고 있다면 = 시작점
            if maze[i][j] == 2:
                sx, sy = i, j

    result = bfs(sx, sy)

    print(f"#{tc} {result}")