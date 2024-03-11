import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*16
dp[0] = 4
for i in range(n):
    dp[i+1] = (2*int(dp[i]**0.5)-1)**2

print(dp[n])