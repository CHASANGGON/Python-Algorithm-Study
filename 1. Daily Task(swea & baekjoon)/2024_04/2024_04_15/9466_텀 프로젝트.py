def dfs(now):
    team.append(now) # 팀 리스트에 추가
    
    visited[now] = 0 # 방문 체크
    
    nxt = graph[now] # nxt 변수 갱신
    
    if visited[nxt]: # 방문한 적 없으면
        return dfs(nxt) # 계속 탐색
    
    # 방문한 적 있는데
    if nxt in team: # 같은 팀 멤버라면 -> 싸이클을 이루는 경우
        return len(team[team.index(nxt):]) # 싸이클을 이루는 만큼만 정답에서 제외시키기 / 자기 자신과 팀이라면 1을 반환하게 됨
    return 0 # 싸이클을 이루지 못한다면 제외 시킬 값이 없음


import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# 입력
t = int(input())
for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().split())) 
    
    visited = [1] * (n+1) # 방문 체크
    
    for i in range(1,n+1):
        if visited[i]: # 방문한 적 없으면
            team = [] # 팀 요소를 기억할 리스트
            n -= dfs(i) # 팀을 이룬 수만큼 빼기
    
    print(n)