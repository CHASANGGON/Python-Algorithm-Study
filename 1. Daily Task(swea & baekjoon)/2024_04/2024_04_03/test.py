from collections import deque
n,k = map(int,input().split())
dist = [-1]*100001
route = [-1]*100001
def bfs(n):
    q = deque()
    q.append(n)
    dist[n] = 0
    while q:
        node= q.popleft()
        if node == k:
            return dist[node]
        for next in [node-1,node+1,node*2]:
            if 0<=next<100001:
                if dist[next] == -1:
                    q.append(next)
                    dist[next] = dist[node] + 1
                    route[next] = node

dist = bfs(n)
print(dist)

result = []
result.append(k)
for i in range(dist):
    result.append(route[result[-1]])
print(*result[::-1],sep=' ')