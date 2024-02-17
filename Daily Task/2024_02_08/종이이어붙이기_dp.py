T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    dp = [0] * 301  # 미리 크기를 301까지 확보한 리스트 0 초기화
    dp[10] = 1
    dp[20] = 3

    for N in range(30, N+1, 10):
    	dp[N] = dp[N - 10] + 2*dp[N - 20]
    
    print(f'#{test_case} {dp[N]}')