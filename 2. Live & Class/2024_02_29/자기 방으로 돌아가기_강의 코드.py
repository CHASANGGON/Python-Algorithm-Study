t = int(input())

for tc in range(1,t+1):

    n = int(input())

    # 복도 리스트 초기화
    corridor = [0] * 401
    max_v = 0

    for _ in range(n):
        # 현재방 s, 돌아갈방 e
        s, e = map(int,input().split())

         # 특징 1번 출발지보다 목적지가 더 큰 값이 되도록 swap
        if s > e: s, e = e, s # swap

        # 특징 2번 아랫방을 윗방으로 변경
        if s % 2 == 0: 
            s -= 1
        if e % 2 == 1:
            e += 1

        for i in range(s, e + 1):
            corridor[i] += 1
            max_v = max(corridor[i], max_v)

    print(f'#{tc} {max_v}')