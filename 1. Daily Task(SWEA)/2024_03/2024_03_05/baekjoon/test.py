T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    ns = list(map(int,input().split()))
    s = sum(ns)
    dp = [0]*(s+1)
    dp[0] = 1
    
    for n in ns:
        for i in range(s,n-1,-1):
            dp[i] += dp[i-n]
        # print(dp)
    print(f'#{tc} {dp[K]}')