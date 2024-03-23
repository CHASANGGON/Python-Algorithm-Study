from collections import deque
import sys
input = sys.stdin.readline

# 참외의 수
n = int(input())

dq = deque()
for _ in range(6):
    d, l = map(int, input().split())
    dq.append([d,l])
    

while True:
    dq.append(dq.popleft())
    if dq[0][0] == dq[2][0] and dq[1][0] == dq[3][0]:
        break

s_x, s_y = dq[1][1], dq[2][1]
b_x, b_y = dq[4][1], dq[5][1]

print(n*(b_x*b_y-s_x*s_y))