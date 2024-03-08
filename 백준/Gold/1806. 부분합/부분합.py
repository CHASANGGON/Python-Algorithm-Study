import sys
input = sys.stdin.readline

N, S = map(int,input().split())
arr = list(map(int,input().split()))

length = N + 1
L, R = 0, 0
s = 0

while 1:
    if s >= S:
        s -= arr[L]
        L += 1
        length = min(length, R - L + 1)
    elif R == N:
        break
    else:
        s += arr[R]
        R += 1

if length == N + 1:
    print(0)
else:
    print(length)