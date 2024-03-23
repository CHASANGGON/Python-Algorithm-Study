def bfs(s, cnt):
    dq = deque()
    dq.append([s, cnt])
    while dq:
        # popleft를 하면 bfs
        # pop을 하면 dfs
        now, cnt = dq.popleft()
        
        # 도착하면
        if now == g:
            # 값을 대입하고(bfs이기 때문에 항상 최소 횟수로 도달한다!! 그래서 그냥 대입!)
            visited[now] = cnt
            # 함수 종료
            return
        
        # up, down을 하나씩 수행
        for nxt in now + u, now - d:
            # 인덱스 검사
            # 이미 방문한 적 있다면, 현재 해당 층에 접근하는 것은 최소 횟수가 아님!
            # 그러므로 실행할 필요가 없다!
            if 0 <= nxt <= f and visited[nxt]:
                visited[nxt] = 0
                dq.append([nxt, cnt + 1]) # 다음 탐색을 위해 큐에 푸쉬

from collections import deque
import sys
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

visited = [1]*(f+1)
visited[0] = 0 # 0층은 존재 x
visited[s] = 0 # 출발층
visited[g] = 'use the stairs' # 도착층에 도착하지 못 한다면 'use the stairs'는 바뀌지 않는다!

bfs(s, 0)
print(visited[g])