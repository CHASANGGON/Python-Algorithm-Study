t = int(input())

def min_fuel_cost(n, arr):
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = 0
    
    # Fill the dp table
    for i in range(n):
        for j in range(n):
            if i > 0:  # Check upward movement
                dp[i][j] = min(dp[i][j], dp[i-1][j] + max(arr[i][j] - arr[i-1][j], 0) + 1)
            if j > 0:  # Check leftward movement
                dp[i][j] = min(dp[i][j], dp[i][j-1] + max(arr[i][j] - arr[i][j-1], 0) + 1)
    
    return dp[n-1][n-1]

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = min_fuel_cost(n, arr)
    print(f'#{tc} {result}')
