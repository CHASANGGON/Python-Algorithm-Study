T = 10

for test_case in range(1,T+1):
    input()
    target = input() # ti
    strs = input() # ~~ti~~
    
    trgt_len = len(target) # 2
    strs_len = len(strs) # 4

    cnt = 0
    for i in range(strs_len-trgt_len+1): # 4-2+1 = 3 -> 0~2
        if target == strs[i:i+trgt_len]: # -> 0:2, 1:3, 2:4
            cnt += 1

    print(f'#{test_case} {cnt}')