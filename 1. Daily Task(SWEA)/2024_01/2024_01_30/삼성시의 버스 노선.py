T = int(input())
 
for test_case in range(1, T + 1):
    bus_station = [0]*5001
    N = int(input())
    
    for _ in range(N):
        A,B = map(int,input().split())
        for i in range(A,B+1):
            bus_station[i] += 1

    P = int(input())
    count = [0]*(P+1)
    for i in range(1,P+1):
        count[i] = bus_station[int(input())]
    count.pop(0)
    print(f'#{test_case}',end=' ')
    print(*count)