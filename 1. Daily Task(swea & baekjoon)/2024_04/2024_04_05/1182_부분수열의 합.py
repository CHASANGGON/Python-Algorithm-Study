def dfs(i, s):
    global cnt
    
    if i == N:
        if s == S:
            cnt += 1
        return
    
    dfs(i+1, s+nums[i])
    dfs(i+1, s)

    
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
if S == 0:
    cnt -= 1
print(cnt)