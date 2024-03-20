import sys
input = sys.stdin.readline

n = int(input())
T, P, dp = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
for i in range(1, n + 1):
    T[i], P[i] = map(int, input().split())
    
    
for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])
    if i + T[i] - 1 <= n:
        dp[i + T[i] - 1] = max(dp[i + T[i] - 1], dp[i - 1] + P[i])

print(dp[n])