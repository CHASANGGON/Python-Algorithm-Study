import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
length = N + 1
s = 0

while True:
    if s >= S:
        length = min(length, right - left)
        s -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        s += arr[right]
        right += 1

if length == N + 1:
    print(0)
else:
    print(length)
