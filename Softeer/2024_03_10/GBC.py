import sys
input = sys.stdin.readline

n, m = map(int,input().split())

speed = [0]*101
now = 1
for _ in range(n):
    d, s = map(int,input().split())
    for i in range(now,now+d):
        speed[i] = s
    now += d

now = 1
for _ in range(m):
    d, s = map(int,input().split())
    for i in range(now,now+d):
        speed[i] -= s
    now += d

print(-min(speed))