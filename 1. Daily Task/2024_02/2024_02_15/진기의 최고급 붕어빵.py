T = int(input())

for test_case in range(1,T+1):
    N, M, K = map(int,input().split()) # 손님, 시간, 개수
    guest = list(map(int,input().split()))
    
    guest.sort()
    guest = [0] + guest
    mission = 'Possible'
    for i in range(1,N+1):
        # 3초에 첫 손님(guest[i]) -> 2초(K)에 2개 생산 < i = 3
        if (guest[i]//M)*K < i:
            mission = 'Impossible'
            break
            
    print(f'#{test_case} {mission}')