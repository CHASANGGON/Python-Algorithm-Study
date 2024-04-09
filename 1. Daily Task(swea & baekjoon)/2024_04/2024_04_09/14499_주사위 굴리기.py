import sys
input = sys.stdin.readline

# 지도 크기 N, M (1 ≤ N, M ≤ 20)
# 주사위 좌표 x, y
# 명령 개수 K
n, m, x, y, k = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
orders = list(map(int, input().split()))

dice = [0,0,0,0,0,0,0] # 전개도의 순서를 참고

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
for order in orders:
    if order == 1: # 동쪽
        if y + 1 >= m: # 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시
            continue
        y += 1
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]
        
    elif order == 2: # 서쪽
        if y - 1 < 0:
            continue
        y -= 1
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]
        
    elif order == 3: # 북쪽
        if x - 1 < 0:
            continue
        x -=1 
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]
        
    else: # 남쪽
        if x + 1 >= n:
            continue
        x += 1
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]
    
    if arr[x][y] == 0: # 칸의 수가 0이면, 주사위 바닥면 -> 칸
        arr[x][y] = dice[6]
    else: # 칸의 수가 0이 아니면, 칸의 수 -> 주사위 바닥면, 칸의 수는 0
        dice[6] = arr[x][y]
        arr[x][y] = 0
    
    print(dice[1])