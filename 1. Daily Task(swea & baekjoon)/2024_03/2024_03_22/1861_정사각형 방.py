def find_max():
    mn_room = 1000000
    mx_distance = 1
    for i in range(n):
        for j in range(n):
            if dp[i][j] > mx_distance:
                mx_distance = dp[i][j] # 최댓값 갱신
                mn_room = arr[i][j] # 방 번호 갱신
            elif dp[i][j] == mx_distance:
                mn_room = min(mn_room, arr[i][j])
    
    return mn_room, mx_distance

def dfs(i, j):
    # dp 조건 1 : 이미 방문했던 곳이라면 더 이상 탐색 x
    if dp[i][j]:
        return dp[i][j]
    
    # 방문한 적 없다면 탐색
    else:    
        dp[i][j] = 1 # dp 조건 2 : 항상 방문 체크
        
        for k in range(4): # 탐색
            ni = i + di[k]
            nj = j + dj[k]
            # 인덱스 검사
            if 0 <= ni < n and 0 <= nj < n:
                # 값 검사
                if arr[i][j] + 1 == arr[ni][nj]:
                    # 방문 검사
                    # dp 조건 3 : 방문 체크를 하면서 기록한 값 1과
	                  # 탐색을 보내서 반환된 값 중 더 큰 값을 "기록"
                    # 항상 기록하기 때문에 한 번 간 곳은 더 이상 재탐색하지 않는다
                    # 또한 방문처리로 끝나는 게 아니라 값도 같이 갱신해준다!
                    dp[i][j] = max(dp[i][j], 1 + dfs(ni,nj))
        return dp[i][j] # dp 조건 4 : 위의 max에서 dfs에서 값을 사용해야하기 때문에 항상 반환

t = int(input())

for tc in range(1, t + 1):

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*n for _ in range(n)]
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    
    for i in range(n):
        for j in range(n):
            if not dp[i][j]:
                dfs(i, j)
        
    mn, mx = find_max()
    
    print(f'#{tc} {mn} {mx}')