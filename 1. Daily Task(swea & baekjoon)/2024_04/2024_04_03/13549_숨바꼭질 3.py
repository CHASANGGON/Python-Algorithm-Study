def bfs(now):
    dq = deque()
    dq.append(now)
    visited[now] = 0
    
    while dq:
        now = dq.popleft()
        if now == k: # 도착
            print(visited[now])
            return

        # 순서가 중요
        # 곱하기는 시간이 추가되지 않으므로 가장 먼저 한다.
        # 그 다음 빼기를 해야한다. 왜그런지 예시를 생각해보자
        # 빼기 먼저   : 4 - 8(0) - 3(1) - 5(1) - 16(0) - 6(1) : 1
        # 더하기 먼저 : 4 - 8(0) - 5(1) - 3(1) - 16(0) - 10(1) - 6(2) : 2
        # 곱하기를 한 다음에(+방향) 다시 빼기(-방향)를 해야 최대한 곱하기를 많이 할 수 있다
        # 곱하기는 시간이 증가하지 않으므로 그래야만 최소 시간을 보장할 수 있다
        
        # 곱하기
        if now * 2 <= 100000 and visited[now*2] == -1:
            visited[now * 2] = visited[now]
            dq.append(now * 2)
        
        # 빼기
        if now - 1 >= 0 and visited[now-1] == -1:
            visited[now - 1] = visited[now] + 1
            dq.append(now - 1)
        
        # 더하기
        if now + 1 <= 100000 and visited[now+1] == -1:
            visited[now + 1] = visited[now] + 1
            dq.append(now + 1)
            

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [-1] * 100001
bfs(n)