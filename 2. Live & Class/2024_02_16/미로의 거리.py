import sys

sys.stdin = open('input.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solution(maze, N):
    # 시작지점2, 도착지점3
    def get_point():
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:
                    sx, sy = i, j
                elif maze[i][j] == 3:
                    ex, ey = i, j
        return sx, sy, ex, ey

    sx, sy, ex, ey = get_point()
    maze[ex][ey] = 0

    # BFS 탐색 방법으로 시작점에서부터 도착지점으로 도달할 수 있는지 확인...!
    def bfs(sx, sy):
        # 미로에다가 내가 방문한 지점을 벽1으로 만들기...!
        # 시작점에 대한 방문 표기..
        queue = []
        maze[sx][sy] = 0  # 방문체크
        queue.append((sx, sy))

        # 큐가 빌 때 까지 (더이상 방문할 수 있는 노드X)
        while queue:
            # 큐에서 좌표값을 하나 꺼내오고
            x, y = queue.pop(0)
            # 해당좌표에서 상하좌우 탐색...
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 좌표가 바깥을 벗어난 경우나, 벽을 만난 경우는 다른 방향으로 탐색 진행/./..
                if 0 > nx or 0 > ny or N <= nx or N <= ny or maze[nx][ny] >= 1:
                    continue
                # (nx, ny) 방문을 해줘야하므로..i
                maze[nx][ny] = maze[x][y] + 1
                # (nx, ny) 좌표가 도착지점일 때(= 3의 값을 가질떄..)
                if ex == nx and ey == ny:
                    return maze[ex][ey]

                queue.append((nx, ny))
        return 0

    # 도착지점에 도달한 경우를
    result = bfs(sx, sy)
    # result 값이 0 이라면 도달하지 못한 경우이다...!
    if result == 0:
        return 0
    else:
        return result - 1


# 테스트케이스 수 T
T = int(input())
for tc in range(1, 1 + T):
    # 입력
    # 미로의 한변이 길이 N
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # 로직
    result = solution(maze, N)
    # 출력
    print(f"#{tc} {result}")