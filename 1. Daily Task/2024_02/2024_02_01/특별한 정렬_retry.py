# 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬 D3
# 버블 정렬
T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    nums = list(map(int,input().split()))

    for i in range(N-1):
        target = nums[i]
        remember = i
        for j in range(i,N):
            if i % 2 == 0: # 최댓값
                if nums[j] > target:
                    target = nums[j]
                    remember = j
            else: # 최솟값
                if nums[j] < target:
                    target = nums[j]
                    remember = j
        nums[i], nums[remember] = nums[remember], nums[i]

    print(f'#{test_case} ',end='')
    for i in range(10):
        print(nums[i],end=' ')
    print()