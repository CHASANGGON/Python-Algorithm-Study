import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

y = 0
m = 0
for a in arr:
    y += (a // 30 + 1)*10
    m += (a // 60 + 1)*15

if y > m:
    print('M', str(m))
elif y < m:
    print('Y', str(y))
else:
    print('Y M', str(y))