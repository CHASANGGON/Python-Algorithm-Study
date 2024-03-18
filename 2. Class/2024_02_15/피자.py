from collections import deque

# 테스트케이스 수 T
T = int(input())
for tc in range(1, T + 1):
    # 입력
    # 화덕의 크기 N, 피자의 개수 M
    N, M = map(int, input().split())
    # 피자들의 각각의 치즈양 pizzas
    pizzas = list(map(int, input().split()))

    # 로직
    # 피자들의 번호와 치즈양을 매칭시켜 다시 저장...
    # for idx in range(M):
    #     c = pizzas[idx]  # 치즈량
    #     pizzas[idx] = [idx + 1, c]  # [인덱스번호, 치즈량]
    # pizzas = [[idx + 1, pizzas[idx]] for idx in range(M)]
    pizzas = [[idx, c] for idx, c in enumerate(pizzas, start=1)]
    # 화덕에 피자를 미리 넣어두겠다...
    # N 만큼 화덕에 피자를 미리 배치...
    furnace = deque(pizzas[:N])
    pizzas = pizzas[N:]

    # 화덕에 모든 피자가 없어질 때까지 반복...!
    while len(furnace) > 0:
        # 화덕에서 피자를 한 판 꺼낸다...!
        idx, c = furnace.popleft()
        # 치즈의 양을 반절 줄여주고..
        c //= 2
        # - 치즈가 다 녹은 경우
        if c == 0:
            # 새로운 피자 투입! (없으면 말고)
            if pizzas:
                furnace.append(pizzas.pop(0))
        # -  //     녹지 않은 경우...
        else:
            # 해당 피자를 다시 투입...!
            furnace.append([idx, c])

    # 출력
    print(f"#{tc} {idx}")