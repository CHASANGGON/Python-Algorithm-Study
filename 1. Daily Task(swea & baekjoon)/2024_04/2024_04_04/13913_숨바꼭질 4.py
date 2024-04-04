def bfs():
    dq = deque()
    dq.append(n)

    while dq:
        now = dq.popleft()
        if now == k:
            return
        for nxt in now+1, now-1, now*2:
            if 0 <= nxt <= 100000 and before[nxt] == -1:
                dq.append(nxt)
                cnt[nxt] = cnt[now] + 1
                before[nxt] = now


from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
before = [-1] * 100001
cnt = [0] * 100001
bfs()
print(cnt[k])


path = [k]
for _ in range(cnt[k]):
    path.append(before[path[-1]])
print(*path[::-1])