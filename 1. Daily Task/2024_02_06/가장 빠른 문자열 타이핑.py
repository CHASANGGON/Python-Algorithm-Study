T = int(input())
for test_case in range(1,T+1):
    a, b = input().split()
    a_l, b_l = len(a), len(b)

    print(f'#{test_case} {a_l-(b_l-1)*a.count(b)}')