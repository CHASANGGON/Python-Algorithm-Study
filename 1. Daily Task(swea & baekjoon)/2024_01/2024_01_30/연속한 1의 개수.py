T = int(input())
 
for test_case in range(1, T + 1):
    input()
    B = input()
    max_len = '1'
    while max_len in B:
        max_len += '1'
    print(f'#{test_case} {len(max_len)-1}')