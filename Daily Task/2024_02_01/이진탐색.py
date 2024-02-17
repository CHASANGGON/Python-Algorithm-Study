T = int(input())

for test_case in range(1,T+1):
    P, A, B = map(int,input().split())
    r_A = r_B = P
    l_A = l_B = 1
    a_count = b_count = 0
    while True:
        c_A = int((l_A+r_A)/2)
        a_count += 1
        if c_A == A:
            break   
        elif c_A > A:
            r_A = c_A
        else:
            l_A = c_A

    while True:
        c_B = int((l_B+r_B)/2)
        b_count += 1
        if c_B == B:
            break   
        elif c_B > B:
            r_B = c_B
        else:
            l_B = c_B

    if a_count < b_count:
        win = 'A'
    elif a_count > b_count:
        win = 'B'
    else:
        win = 0

    print(f'#{test_case} {win}')