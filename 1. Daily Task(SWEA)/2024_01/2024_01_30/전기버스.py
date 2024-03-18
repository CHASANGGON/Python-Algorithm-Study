T = int(input())
    
for test_case in range(1, 1+T):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    print(f'#{test_case} ',end='')

    count = 0    
    now = 0
    i = 0
    
    if station[-1] + K < N or now + K < station[i]:
        pass
    else:
        while 1:
            if now + K >= N: # 도착
                break
            if now + K < station[i]:
                count = 0
                break
            while now + K >= station[i]: # 어디 정류장까지 갈 수 있을지
                i += 1
                if i == M:
                    break
            i -= 1

            now = station[i] # 충전
            count += 1
            i += 1
    print(count)