t = int(input())

for tc in range(1,t+1):
    charge = list(map(int, input().split())) # 1일, 1달, 3달, 1년
    days_of_use = list(map(int, input().split()))
    
    dp = [0]*12
    dp[11] = charge[3]
    
    for i in range(12):
        if days_of_use[i]:
            dp[i] = min(dp[i] + charge[0]*days_of_use[i], dp[i] + charge[1], dp[i] + charge[2])
            if i <= 8:
                dp[i + 3] += charge[2]
            if i <= 9:
                dp[i + 2] += charge[2]
            
    print(f'#{tc} {dp[11]} ')