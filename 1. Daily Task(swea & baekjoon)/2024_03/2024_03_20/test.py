def dp_f(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        dp[a][b][c] = dp_f(20,20,20)
        return dp[a][b][c]
    elif a < b and b < c :
        dp[a][b][c] = dp_f(a,b,c-1) + dp_f(a,b-1,c-1) - dp_f(a,b-1,c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = dp_f(a-1,b,c) + dp_f(a-1,b-1,c) + dp_f(a-1,b,c-1) - dp_f(a-1,b-1,c-1)
        return dp[a][b][c]

dp = [[[0 for _ in range(51)] for _ in range(51)] for _ in range(51)]
dp_f(50,50,50)

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print(f'w({a}, {b}, {c}) = {dp[a][b][c]}')