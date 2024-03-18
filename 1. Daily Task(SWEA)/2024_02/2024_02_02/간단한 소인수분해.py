# 2a x 3b x 5c x 7d x 11e
T = int(input())

for test_case in range(1,1+T):
    n = int(input())
    list_2_3_5_7_11 = [0]*5

    while n % 2 == 0:
        n //= 2
        list_2_3_5_7_11[0] += 1

    while n % 3 == 0:
        n //= 3
        list_2_3_5_7_11[1] += 1

    while n % 5 == 0:
        n //= 5
        list_2_3_5_7_11[2] += 1

    while n % 7 == 0:
        n //= 7
        list_2_3_5_7_11[3] += 1

    while n % 11 == 0:
        n //= 11
        list_2_3_5_7_11[4] += 1

    print(f'#{test_case} ', end='')
    print(*list_2_3_5_7_11)
