def find_max_sum(N, M, arr):
    sum_max = 0
    start_x, start_y = 0, 0
    before_local_max = 0
    while True:
        local_max = 0
        next_x = 0
        next_y = 0

        # 탐색 범위 설정
        for x in range(start_x, min(start_x + M, N)):
            for y in range(start_y, min(start_y + M, N)):
                if arr[x][y] > local_max:
                    local_max = arr[x][y]
                    next_x, next_y = (x, y)

        if local_max == before_local_max:
            break

        start_x, start_y = next_x, next_y
        sum_max += local_max
        
        before_local_max = local_max

    return sum_max


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = find_max_sum(N, M, arr)
    print(f'#{tc} {result}')