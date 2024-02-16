T = int(input())

for test_case in range(1,T+1):

    n = int(input())

    nums = list(map(int,input().split()))
    monotonic_increase = []
    for i in range(n-1):
        for j in range(i+1,n):
            multiple = list(str(nums[i]*nums[j]))
            before = int(multiple[0])
            is_monotic = True
            for m in multiple:
                if before > int(m):
                    is_monotic = False
                before = int(m)
            if is_monotic:
                monotonic_increase.append(nums[i]*nums[j])
    
    if monotonic_increase:
        result = max(monotonic_increase)
    else:
        result = -1

    print(f'#{test_case} {result}')