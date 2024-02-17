T = int(input())

for test_case in range(1,T+1):
    input()
    nums = list(map(int,input().split()))
    

    max_num, min_num = nums[0], nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    print(f'#{test_case} {max_num-min_num}')