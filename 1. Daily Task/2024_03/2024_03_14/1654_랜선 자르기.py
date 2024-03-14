import sys
input = sys.stdin.readline

n, k = map(int,input().split())

arr = [0]*n
for i in range(n):
    arr[i] = int(input())

l, r = 1, min(arr)
ans = 0
while l <= r:
    c = (l+r)//2
    s = 0
    for i in range(n):
        s += arr[i] // c
    if s >= k:
        ans = max(c,ans)
        l = c + 1
    elif s < k:
        r = c - 1

print(ans)