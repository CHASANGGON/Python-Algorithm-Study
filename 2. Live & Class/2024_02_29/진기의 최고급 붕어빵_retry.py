t = int(input())

for tc in range(1,t+1):

    # 손님 n명 / m초에 / k개
    n, m, k = map(int,input().split())
    guest = list(map(int,input().split()))
    guest.sort()

    result = 'Possible'

    for i in range(n):
        # ((i+1)번 째 손님 방문 시간 // m초) * k개
        # -> i+1 번 째 손님 방문시 만들 수 있는 개수
        # < i+1 개 필요(i+1번 째 손님 방문시)
        if (guest[i] // m) * k < i + 1:
            result = 'Impossible'
            break
    
    print(f'#{tc} {result}')