# N-Queen

# 중첩 함수(nested function): 내부 함수를 만들어서 간단하게 정리...!
def n_queen_solve(N):
    # 내가 해당 (row, col)에 퀸을 배치할 수 있는지 체크...!
    # 대각선에 대해서 서로 영역이 겹치지 않는지만 간단하게 체크!
    def check(row, col):
        # 이전까지 놓아져 있는 퀸이
        for x in range(row): # [0, row)
            y = board[x]
            # 내가 놓으려고 하는 (row, col)의 위치와 대각선 영역이 서로 겹치는가!
            if abs(x - row) == abs(y - col):
                return False # 놓을 수가 없어요!
        
        # 해당 위치에는 퀸을 배치할 수 있다!
        return True
    
    
    # 완전 탐색 (DFS)
    def dfs(depth):
        nonlocal cnt, visited, board
        # 기저 조건(종료 조건) : depth가 Queen의 개수 만큼 카운트가 되었을 때
        # -> 퀸이 N개 놓여져 있을 때 중단하겠다..!
        if depth == N:    
            cnt += 1 # Queen이 올바르게 배치되어 있는 경우 카운트 +1
            return
        
        # 재귀적으로 말을 배치...!
        # 반복문을 통해서 1부터 N번까지의 모든 위치에 말을 놓아보도록 시도..!
        for col in  range(N):
            # 해당 행에 Queen을 배치...! (depth, col)
            # 해당 위치에 배치를 할 수 있는지 체크!
            if not visited[col] and check(depth, col):
                board[depth] = col
                # visited 배열을 통해서 동일한 행에 대해 다른 Queen이 들어가지 않도록 체크
                visited[col] = True # 결정
                dfs(depth + 1)
                visited[col] = False # 복구
        
    # 카운트 변수(global)
    cnt = 0
    visited = [False] * N
    # 배치할 말의 위치 board
    board = [-1] * N

    dfs(0)
    
    return cnt
    

# N-Queen을 놓을 수 있는 횟수를 카운트하여 출력...!
N = int(input())

cnt = n_queen_solve(N)

print(cnt)