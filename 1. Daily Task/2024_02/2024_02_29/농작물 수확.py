def out_of_range(ni,nj):
    return 0 <= ni < n and 0 <= nj < n

def bfs(q):
    global s

    # 1겹씩 bfs탐색을 위해 새로운 큐 생성
    new_q = []

    while q:
        i, j = q.pop(0)
        
        # 델타 탐색
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            
            # 인덱스 체크 및 visited 체크
            if out_of_range(ni,nj) and arr[ni][nj] != -1:
                s += arr[ni][nj] # 누적합
                arr[ni][nj] = -1 # visited
                new_q.append([ni,nj]) # 추가 탐색을 위해 enque
    
    return new_q

t = int(input())

for tc in range(1,t+1):
    n = int(input())

    arr = [list(map(int,input())) for _ in range(n)]

    # 델타 생성
    di = [1,-1,0,0]
    dj = [0,0,1,-1]

    # 수익을 저장할 변수
    s = arr[n//2][n//2]

    # visited의 의미 = -1
    arr[n//2][n//2] = -1
    
    # q 초기화
    q = [[n//2,n//2]]

    # n//2 번 BFS
    for _ in range(n//2):
        q = bfs(q)

    print(f'#{tc} {s}')