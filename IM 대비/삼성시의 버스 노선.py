# 5,000개의 버스 정류장
# 버스 노선은 N개
# i번째 버스 노선은 번호가 Ai이상이고, Bi이하인 모든 정류장만을 다니는 버스 노선
# ->
# P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    bus_station = [0]*5001
    
    for _ in range(N):
        A, B = map(int,input().split())
        for i in range(A,B+1):
            bus_station[i] += 1
    
    P = int(input())
    result = []
    for i in range(P):
        result.append(bus_station[int(input())])
    
    print(f'#{test_case} ',end='')
    print(*result)