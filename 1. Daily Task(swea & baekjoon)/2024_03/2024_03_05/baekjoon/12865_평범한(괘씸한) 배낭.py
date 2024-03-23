import sys
input = sys.stdin.readline

# 입력 1
n, k = map(int,input().split())

# 입력 2
wv = []
for _ in range(n):
    w, v = map(int,input().split())
    wv.append([w,v])

# 배낭의 최댓값
dp = [0]*(k+1)

# dp 계산
for w, v in wv:
    for i in range(k,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v)
    
print(dp[k])