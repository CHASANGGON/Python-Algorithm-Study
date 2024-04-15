t = int(input())

for _ in range(t):
    n = int(input())
    
    graph = [0] + list(map(int, input().split()))
    visited = [1] * (n+1)
    
    cnt = 0
    for i in range(1,n+1):
        if visited[i]:
            cnt += 1
            
            visited[i] = 0
            stack = [i]
            
            while stack:
                now = stack.pop()
                
                if visited[graph[now]]:
                    visited[graph[now]] = 0
                    stack.append(graph[now])
    print(cnt)