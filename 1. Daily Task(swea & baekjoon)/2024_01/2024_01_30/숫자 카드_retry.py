# # # 간단한 소인수분해
# T = int(input())

# for test_case in range(1,T+1):
#     N = int(input())
#     div_list = [2, 3, 5, 7, 11]
#     quo_list = []
#     for i in range(len(div_list)):
#         quo_cnt = 0
#         while N % div_list[i] == 0:
#             N //= div_list[i]
#             quo_cnt += 1
#         quo_list.append(quo_cnt)

#     print(f'#{test_case} ',end='')
#     print(*quo_list)



# # # 삼성시의 버스 노선
# T = int(input())

# for test_case in range(1,T+1):
#     N = int(input())
#     bus_station = [0]*5001
#     for i in range(N):
#         A, B = map(int,input().split())
#         for j in range(A,B+1):
#             bus_station[j] += 1
    
#     P = int(input())
#     show_me_the_cnt = []
#     for i in range(P):
#         show_me_the_cnt.append(int(input()))
    
#     print(f'#{test_case} ',end='')
#     for i in range(P):
#         print(bus_station[show_me_the_cnt[i]],end=' ')
#     print()



# # 연속한 1의 개수
# case1 - 문자열로 처리
# T = int(input())

# for test_case in range(1,T+1):
#     input()
#     this_is_stirng = input()

#     i_want_find_this = '1'

#     while i_want_find_this in this_is_stirng:
#         i_want_find_this += '1'
    
#     print(f'#{test_case} {len(i_want_find_this)-1}')

# # # 연속한 1의 개수
# # case1 - 숫자로 처리
# T = int(input())

# for test_case in range(1,T+1):
#     N = int(input())
#     strs = input().strip()

#     nums = []
#     for s in strs:
#         nums.append(int(s))
    
    
#     cnt, max_len = 0, 0
#     for i in range(N):
#         if nums[i] == 1:
#             cnt += 1
#         elif nums[i] == 0:
#             cnt = 0
#         max_len = max(cnt,max_len)

#     print(f'#{test_case} {max_len}')



# 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드
# 카운팅 정렬인가~?
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    nums = list(map(int,input()))
    cnt_list = [0]*10

    for num in nums:
        cnt_list[num] += 1
    # 리스트를 순회하며, max값 "이상"의 값을 max에 갱신
    max_cnt = cnt_list[0]
    max_num = 0
    for i in range(10):
        if cnt_list[i] >= max_cnt:
            max_cnt = cnt_list[i]
            max_num = i

    print(f'#{test_case} {max_num} {max_cnt}')