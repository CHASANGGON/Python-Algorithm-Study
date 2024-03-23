def dfs(i, s):
    global cnt
    if s > k:
        return
    if s == k:
        cnt += 1
        return
    
    if i == n:
        return
    
    dfs(i + 1, s)
    dfs(i + 1, s + nums[i])

t = int(input())

for tc in range(1, t + 1):

    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    cnt = 0
    dfs(0, 0) # 깊이, 합
    
    print(f'#{tc} {cnt}')