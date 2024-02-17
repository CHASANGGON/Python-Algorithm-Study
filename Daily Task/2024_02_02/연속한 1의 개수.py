T = int(input())
for test_case in range(1,1+T):
    input()
    word = input()

    one_str = '1'
    
    while True:
        if one_str in word:
            one_str += '1'
        else:
            break
    
    print(f'#{test_case} {len(one_str)-1}')