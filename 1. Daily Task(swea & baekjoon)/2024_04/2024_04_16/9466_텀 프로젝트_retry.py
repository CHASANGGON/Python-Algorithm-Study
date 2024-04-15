import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    
    n = int(input())
    graph = [0] + list(map(int, input().split())) 
    
    visited = [1] * (n+1) # 방문 체크
    
    for i in range(1,n+1):
        if graph[i] == i: # 1인 팀은 제외
            visited[i] = 0 # 방문 체크
            n -= 1
            
    for start in range(1,n+1):
        if visited[start]: # 아직 방문한 적 없다면
            visited[start] = 0 # 방문 체크
            stack = [start]
            team = [start]
            
            while stack:
                now = stack.pop()
                nxt = graph[now]
                
                if visited[nxt]:
                    visited[nxt] = 0
                    team.append(nxt)
                    stack.append(nxt)
                    
            if nxt in team: # nxt가 team에 포함되어 있다면 
                n -= len(team[team.index(nxt):]) # 해당 싸이클만큼 제외
    
    print(n)