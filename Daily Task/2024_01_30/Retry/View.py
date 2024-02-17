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



# # 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드
# # 카운팅 정렬인가~?
# T = int(input())
# for test_case in range(1,T+1):
#     N = int(input())
#     nums = list(map(int,input()))
#     cnt_list = [0]*10

#     for num in nums:
#         cnt_list[num] += 1
#     # 리스트를 순회하며, max값 "이상"의 값을 max에 갱신
#     max_cnt = cnt_list[0]
#     max_num = 0
#     for i in range(10):
#         if cnt_list[i] >= max_cnt:
#             max_cnt = cnt_list[i]
#             max_num = i

#     print(f'#{test_case} {max_num} {max_cnt}')



# 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스 D3
# 1 내가 짠 코드
# T = int(input())
# for test_case in range(1,T+1):
#     K, N, M = map(int,input().split())
#     station = list(map(int,input().split()))

#     # 현재 위치에서 갈 수 있는 최대거리에서부터
#     # 1-if : 당연히 N에 도착하면 종료
#     # for문을 통하여 최대한 먼 station을
#     # 2-1-elif-if : 발견하면 거기로 위치 갱신 + staion들린 횟수 +
#     # 2-2 : 만약 못 찾으면 탈출
#     # 
#     now = 0
#     cnt = 0
#     charge, not_arrival = True, True
#     while charge and not_arrival:
#         charge = False
#         if now + K >= N:
#             not_arrival = False
#         else:
#             for i in range(K,0,-1): # <now(현재 위치) + 1~K> 범위에서  staion을 탐색
#                 if now + i in station:
#                     idx = station.index(now+i)
#                     now = station[idx]
#                     cnt += 1
#                     charge = True
#                     break
    
#     if not_arrival:
#         cnt = 0
                    
#     print(f'#{test_case} {cnt}')

# 깅대의 코드
# T = int(input())
# for test_case in range(1,T+1):
#     K, N, M = map(int,input().split())
#     station = list(map(int,input().split()))

#     now, cnt = 0, 0
#     while now + K < N:
#         charge = False #  여기서 초기화를 계속 해줘야 하는데, while문 위에서 초기화를 해서 깅대의 노션에 올라온 코드는 탈출을 못 함
#         for i in range(K,0,-1): # <now(현재 위치) + 1~K> 범위에서  staion을 탐색
#             if now + i in station:
#                 now += i # 굳이 인덱스를 찾아줄 필요가 없었다.. 너무나 당연한 것..
#                 cnt += 1
#                 charge = True
#                 break
#         if not charge:
#             cnt = 0 # 이러면 아래에서 따로 cnt = 0 초기화 안 해도 되네..
#             break
            
#     print(f'#{test_case} {cnt}')



#  1206. [S/W 문제해결 기본] 1일차 - View (선택) D3
T = 10
for test_case in range(1,T+1):
    N = int(input())
    apts = list(map(int,input().split()))

    If_I_can_see_I_wll_be_happy = 0
    for i in range(2,N-2):
        can_I_see = apts[i] - max(apts[i-1],apts[i-2],apts[i+1],apts[i+2])
        if can_I_see > 0:
            If_I_can_see_I_wll_be_happy += can_I_see

    print(f'#{test_case} {If_I_can_see_I_wll_be_happy}')