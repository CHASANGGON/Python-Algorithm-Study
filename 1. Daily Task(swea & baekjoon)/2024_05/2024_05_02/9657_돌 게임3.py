import sys
inpput = sys.stdin.readline

n = int(input())
dp = ['X', 'SK', 'CY', 'SK', 'SK', 'SK']

if n > 5:
    for i in range(6, n+1):
        if 'CY' in dp[i-1] or 'CY' in dp[i-3] or 'CY' in dp[i-4]:
            dp.append('SK')
        else:
            dp.append('CY')

print(dp[n])