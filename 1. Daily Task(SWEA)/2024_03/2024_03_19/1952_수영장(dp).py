t = int(input())

for tc in range(1,t+1):
    charge = list(map(int, input().split())) # 1일, 1달, 3달, 1년
    days_of_use = [0] + list(map(int, input().split()))
    
    dp = [0]*13
      
    for i in range(1,13):
        dp[i] = min(dp[i-1] + days_of_use[i] * charge[0], dp[i-1] + charge[1]) # 1일, 1달
        
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + charge[2])
        
    print(f'#{tc} {min(dp[12], charge[3])} ')