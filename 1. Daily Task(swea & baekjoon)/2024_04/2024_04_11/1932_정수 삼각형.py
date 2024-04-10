import sys
input = sys.stdin.readline

n = int(input())

dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1,n):
    dp[i][0] += dp[i-1][0]
    dp[i][i] += dp[i-1][i-1]

for i in range(1,n-1):
    for j in range(1,i+1):
        dp[i+1][j] = max(dp[i+1][j] + dp[i][j-1], dp[i+1][j] + dp[i][j])

print(max(dp[n-1]))