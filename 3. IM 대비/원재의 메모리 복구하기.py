T = int(input())

for test_case in range(1,T+1):
    bit = input()
    
    change = 0
    before  = '0' # 초기값은 000 -> 바뀐 횟수를 count
    for b in bit:
        if before != b:
            change += 1
        before = b
    
    print(f'#{test_case} {change}')