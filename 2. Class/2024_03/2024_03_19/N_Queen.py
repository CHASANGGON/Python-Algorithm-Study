# N-Queen

# 완전 탐색 (DFS)
def dfs(depth):
    global cnt
    # 기저 조건(종료 조건) : depth가 Queen의 개수 만큼 카운트가 되었을 때
    # -> 퀸이 N개 놓여져 있을 때 중단하겠다..!
    if depth == N:
        # TOOD : 퀸이 올바르게 놓여져 있는지를 대각선 체크...!
        # 좌하단, 우하단에 퀸이 서로 겹치는 영역을 확인...!
        # Queen을 두 개 가져와서 서로 비교(x1, y1), (x2, y2)
        for x1 in range(N):
            y1 = board[x1]
            for x2 in range(x1+1, N):
                y2 = board[x2]
                # 퀸의 위치를 비교...!
                # X축과 Y축에 대한 거리가 서로 같다면 = 대각선에 있는 것이다..!
                if abs(x1 - x2) == abs(y1 - y2):
                    return 
            
        cnt += 1 # Queen이 올바르게 배치되어 있는 경우 카운트 +1
        return
    
    # 재귀적으로 말을 배치...!
    # 반복문을 통해서 1부터 N번까지의 모든 위치에 말을 놓아보도록 시도..!
    for col in  range(N):
        # 해당 행에 Queen을 배치...! (depth, col)
        # 해당 위치에 배치를 할 수 있는지 체크!
        if not visited[col]:
            board[depth] = col
            # visited 배열을 통해서 동일한 행에 대해 다른 Queen이 들어가지 않도록 체크
            visited[col] = True # 결정
            dfs(depth + 1)
            visited[col] = False # 복구
    

# N-Queen을 놓을 수 있는 횟수를 카운트하여 출력...!
N = int(input())
# 카운트 변수(global)
cnt = 0
visited = [False] * N
# 배치할 말의 위치 board
board = [-1] * N
dfs(0)
print(cnt)