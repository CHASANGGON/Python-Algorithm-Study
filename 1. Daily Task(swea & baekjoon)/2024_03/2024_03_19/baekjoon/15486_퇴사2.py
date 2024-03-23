import sys
input = sys.stdin.readline

n = int(input())
T, P, dp = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
for i in range(1, n + 1):
    T[i], P[i] = map(int, input().split())
    
    
for today in range(1, n + 1):
    # 어제까지 벌어놓은 돈
    dp[today] = max(dp[today], dp[today - 1])
    
    # 오늘 일을하면, 정산 받는 날
    if today + T[today] - 1 <= n:
        # 이전에 일을해서 정산 받은 돈, 어제까지 벌어놓은 돈 +  오늘 일해서 정산 받을 돈
        dp[today + T[today] - 1] = max(dp[today + T[today] - 1], dp[today - 1] + P[today])
        print(dp)
print(dp[n])