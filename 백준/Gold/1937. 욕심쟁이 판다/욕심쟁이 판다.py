# 현재 값보다 큰 값으로만 이동 -> 상당한 욕심쟁이 : 그리디인가? BFS인가? DFS인가?
# 최대한 많은 칸을 방문하는 것이 고민
# 최댓값을 계속 갱신해야 하니까 백트래킹이 불가능할 거라는 나의 생각 일단 ㅇㅅㅇ..
# 일단은 모든 좌표에서 완탐을 해야할 듯
# 아 물론 미로에서도 불가능한 경로는 원천봉쇄했는데, 그것도 백트래킹에 해당했으니
# 여기서 말하는 백트래킹도 그것을 말하는 걸지도?
def out_of_range(ni,nj,n):
    return 0 <= ni < n and 0 <= nj < n

def dfs(i,j):
    global max_distance
    # 거리 정보가 확인되지 않으면(방문하지 않았으면) 실행
    if distance[i][j]:
        return distance[i][j]
    else:
        distance[i][j] = 1
        
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if out_of_range(ni,nj,n) and bamboo[i][j] < bamboo[ni][nj]:
                distance[i][j] = max(dfs(ni,nj)+1,distance[i][j])
                # max_distance = max(distance[i][j], max_distance)
    return distance[i][j]
    
    
import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

n = int(input())

bamboo = [list(map(int,input().split())) for _ in range(n)]

# 방문하지 않은 곳은 0
distance = [[0]*n for _ in range(n)]
max_distance = 0
di = [1,-1,0,0]
dj = [0,0,1,-1]
for i in range(n):
    for j in range(n):
        # 방문하지 않은 경우만 실행
        if not distance[i][j]:
            dfs(i,j)

print(max(sum(distance, [])))