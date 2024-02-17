# # 간단한 소인수분해
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    div_list = [2, 3, 5, 7, 11]
    quo_list = []
    for i in range(len(div_list)):
        quo_cnt = 0
        while N % div_list[i] == 0:
            N //= div_list[i]
            quo_cnt += 1
        quo_list.append(quo_cnt)

    print(f'#{test_case} ',end='')
    print(*quo_list)
