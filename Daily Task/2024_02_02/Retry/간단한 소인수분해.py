# 2a x 3b x 5c x 7d x 11e
T = int(input())

for test_case in range(1,1+T):
    n = int(input())
    list_2_3_5_7_11_count = [0]*5
    list_2_3_5_7_11 = [2,3,5,7,11]
		
    for i in range(len(list_2_3_5_7_11)):
        while n % list_2_3_5_7_11[i] == 0:
            n //= list_2_3_5_7_11[i]
            list_2_3_5_7_11_count[i] += 1

    print(f'#{test_case} ', end='')
    print(*list_2_3_5_7_11_count)