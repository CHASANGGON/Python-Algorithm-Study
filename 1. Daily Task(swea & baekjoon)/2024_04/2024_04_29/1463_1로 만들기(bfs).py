from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
lst = [0] * (n+1)
lst[n] = 0
dq = deque()
dq.append(n)

while dq:
    now = dq.popleft()
    if now == 1:
        print(lst[now])
        break
    
    if now % 3 == 0 and lst[now//3] == 0:
        lst[now//3] = lst[now] + 1
        dq.append(now//3)
    
    if now % 2 == 0 and lst[now//2] == 0:
        lst[now//2] = lst[now] + 1
        dq.append(now//2)
        
    if lst[now-1] == 0:
        lst[now-1] = lst[now] + 1
        dq.append(now-1)