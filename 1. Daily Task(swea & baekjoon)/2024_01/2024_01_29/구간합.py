T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    nums = list(map(int,input().split()))
    
    sum_list = [sum(nums[:M])]
    for i in range(N-M): 
        new_sum = sum_list[i] - nums[i] + nums[i+M]
        sum_list.append(new_sum)
        
    print(f'#{test_case} {max(sum_list)-min(sum_list)}')