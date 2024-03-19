t = int(input())
 
for tc in range(1,t+1):
     
    a = list(map(int,input().split()))
     
    n, charge = a[0], a[1:]
     
    dp = [100] * n
    dp[0] = -1
     
    for i in range(n-1):
        for j in range(1, charge[i] + 1):
            if i + j < n:
                dp[i + j] = min(dp[i + j], dp[i] + 1)
    print(f'#{tc} {dp[n-1]}')