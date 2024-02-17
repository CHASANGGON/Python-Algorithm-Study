# # 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬 D3
# # 버블 정렬
# T = int(input())

# for test_case in range(1,T+1):
#     N = int(input())

#     nums = list(map(int,input().split()))

#     for i in range(N-1):
#         target = nums[i]
#         remember = i
#         for j in range(i,N):
#             if i % 2 == 0: # 최댓값
#                 if nums[j] > target:
#                     target = nums[j]
#                     remember = j
#             else: # 최솟값
#                 if nums[j] < target:
#                     target = nums[j]
#                     remember = j
#         nums[i], nums[remember] = nums[remember], nums[i]

#     print(f'#{test_case} ',end='')
#     for i in range(10):
#         print(nums[i],end=' ')
#     print()



# # 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색 D2
# T = int(input())

# for test_case in range(1,T+1):
#     P, A, B = map(int,input().split())
    
#     al, ar, bl, br = 1, P, 1, P
#     a_cnt, b_cnt = 0, 0
    
#     while al <= ar:
#         ca = int((al+ar)/2)
#         a_cnt += 1

#         if ca == A:
#             break
#         elif ca < A:
#             al = ca
#         else:
#             ar = ca

    
#     while bl <= br:
#         cb = int((bl+br)/2)
#         b_cnt += 1

#         if cb == B:
#             break
#         elif cb < B:
#             bl = cb
#         else:
#             br = cb

#     print(f'#{test_case}',end=' ')
#     if a_cnt < b_cnt:
#         print('A')
#     elif a_cnt > b_cnt:
#         print('B')
#     else:
#         print(0)



# # 풍선팡 D2
# T = int(input())
# for test_case in range(1,T+1):
#     N, M = map(int,input().split())

#     balloons = [list(map(int,input().split())) for _ in range(N)]
#     di = [1,-1,0,0]
#     dj = [0,0,1,-1]

#     max_burst = 0
#     for i in range(N):
#         for j in range(M):
#             burst = balloons[i][j]
#             for k in range(1,burst+1):
#                 for d in range(4):
#                     if 0 <= i + k*di[d] <= N-1 and 0 <= j + k*dj[d] <= M-1:
#                         burst += balloons[i+k*di[d]][j+k*dj[d]]
#             max_burst = max(max_burst,burst)

#     print(f'#{test_case} {max_burst}')



# 숫자 배열 회전 D2
def rotation(arr, N):
    arr_90 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_90[j][N-1-i] = arr[i][j]
    return arr_90

T = int(input())
for test_case in range(1,T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]
    
    arr_90 = rotation(arr,N)
    arr_180 = rotation(arr_90,N)
    arr_270 = rotation(arr_180,N)
    print(f'#{test_case}')
    for i in range(N):
        print(''.join(map(str,arr_90[i])), sep='',end =' ')
        print(''.join(map(str,arr_180[i])), sep='',end =' ')
        print(''.join(map(str,arr_270[i])), sep='')