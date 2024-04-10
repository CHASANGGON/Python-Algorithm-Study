import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def dfs(idx, depth, lst):
    if depth == m:
        print(*lst)
    else:
        prev = 0
        for i in range(idx, n):
            if arr[i] != prev:
                dfs(i, depth+1, lst + [arr[i]])
                prev = arr[i]
v = [1]*n
dfs(0, 0, [])