import sys

sys.stdin = open('sample_input.txt', 'r')

dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


# (x, y) 좌표로부터 i 방향으로
# 상대방돌이 사이에 껴 있다면...
# 이 돌들을 나의 돌로 바꾸기...!
def check(boards, N, x, y, color, dir):
    stack = []

    # 편의를 위해서 한칸만 이동 (상대방돌들을 확인...)
    x = x + dx[dir]
    y = y + dy[dir]

    while True:
        # 보드판을 벗어난 경우... 빈 영역을 만난 경우는 탐색 종료
        if 0 > x or x >= N or 0 > y or y >= N or boards[x][y] == 0:
            return
        # 나의 돌이 있는 경우 (공격이 가능)
        elif boards[x][y] == color:
            break
        # 상대돌이 있는 경우
        elif boards[x][y] != color:
            stack.append((x, y))
            x = x + dx[dir]
            y = y + dy[dir]

    # 내가 공격할 수 있는 상황이라면 (돌을 가져갈 수 있는 상황)
    # 스택 안의 모든 돌을 나의 돌로 변경...
    for x, y in stack:
        boards[x][y] = color


def solution(N, M, choices):
    # N * N 크기의 보드판...
    boards = [[0] * N for _ in range(N)]
    middle = N // 2
    # 1을 흑돌, 2를 백돌
    boards[middle - 1][middle - 1] = 2
    boards[middle][middle] = 2
    boards[middle - 1][middle] = 1
    boards[middle][middle - 1] = 1

    # 좌표(x,y)에 대해서 color돌을 놓는다...!
    for x, y, color in choices:
        # 좌표(x,y)에 대해서 color돌을 놓는다..
        boards[x - 1][y - 1] = color
        # 8방 탐색... (상대돌을 가져온다..)
        for i in range(8):
            check(boards, N, x - 1, y - 1, color, i)

    # 백돌과 흑돌의 수를 카운트
    w_cnt = 0
    b_cnt = 0
    for i in range(N):
        for j in range(N):
            if boards[i][j] == 1:
                b_cnt += 1
            elif boards[i][j] == 2:
                w_cnt += 1

    return b_cnt, w_cnt


# 테스트케이스 수 T
T = int(input())
for tc in range(1, T + 1):
    # 입력
    # 보드의 한변의 길이 N, 돌을 놓는 횟수 M
    N, M = map(int, input().split())
    choices = [list(map(int, input().split())) for _ in range(M)]

    # 로직
    b, w = solution(N, M, choices)

    # 출력
    print(f"#{tc} {b} {w}")