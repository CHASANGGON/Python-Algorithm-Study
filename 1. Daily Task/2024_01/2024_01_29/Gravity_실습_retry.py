# # [파이썬 S/W 문제해결 기본] 1일차 - min max 
# # T = int(input())

# # for test_case in range(1,T+1):
# #     input()
# #     nums = list(map(int,input().split()))
    

# #     max_num, min_num = nums[0], nums[0]
# #     for num in nums:
# #         if num > max_num:
# #             max_num = num
# #         if num < min_num:
# #             min_num = num
# #     print(f'#{test_case} {max_num-min_num}')



# # 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합
# T = int(input())

# for test_case in range(1,T+1):
#     N, M = map(int,input().split())
#     nums = list(map(int,input().split()))
    
#     sum_list = [sum(nums[:M])]
#     for i in range(N-M): # 5 - 3 = 2 -> 0, 1
#         new_sum = sum_list[i] - nums[i] + nums[i+M]
#         sum_list.append(new_sum)
        
#     print(f'#{test_case} {max(sum_list)-min(sum_list)}')



# Gravity_실습
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    boxes = list(map(int,input().split()))
    boxes_drop_list = []

    for i in range(N):
        cnt = 0
        for j in range(i+1,N):
            if boxes[i] > boxes[j]:
                cnt += 1
        boxes_drop_list.append(cnt)
        
    print(f'#{test_case} {max(boxes_drop_list)}')