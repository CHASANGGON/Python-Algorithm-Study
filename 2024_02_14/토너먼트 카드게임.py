# 테스트 케이스 수 T
T = int(input())
for tc in range(1, T + 1):
    # 입력
    # 인원의 수 N
    N = int(input())
    # 인원들이 뽑은 카드 번호들 cards
    cards = list(map(int, input().split()))


    # 로직
    # 해당 인원들을 절반씩 자르면서 토너먼트 형태로 경기를 진행...!
    # 분할 - 정복 (divide-conquer) 기법...
    def tournament(i, j):  # 시작점 i, 끝점 j
        # 기저조건 : 단 한명만 남을 때까지...
        if i == j:  # 단 1명만 남은 경우...
            return i  # 자기자신을 반환
        # 해당 인원을 절반씩 자르는 "분할" 과정...
        winner1 = tournament(i, (i + j) // 2)  # 왼쪽 그룹
        winner2 = tournament((i + j) // 2 + 1, j)  # 오른쪽 그룹

        # 가위바위보 게임을 시킨다 "정복"
        winner = play(winner1, winner2)
        return winner


    # 사람 a 와 사람 b에 대한 가위바위보 진행...
    def play(a, b):
        card_a = cards[a]
        card_b = cards[b]

        # 가위1 vs 가위1
        # 바위2 vs 바위2
        # 보 3  vs 보3
        if card_a == card_b:  # 비긴 경우...
            return a
        # a가 이긴경우
        # 가위1 vs 보3
        # 바위2 vs 가위1
        # 보 3  vs 바위2
        elif (card_a == 1 and card_b == 3) or \
                (card_a == 2 and card_b == 1) or \
                (card_a == 3 and card_b == 2):
            return a
        else:
            # a가 진경우
            # 가위1 vs 바위2
            # 바위2 vs 보3
            # 보 3  vs 가위1
            return b

    # [0 ~ N-1] -> 1 ~ N 번 참가자...
    result = tournament(0, N - 1) + 1
    # 출력
    print(f'#{tc} {result}')