# 리스트 슬라이싱을 사용한 풀이
T = 10
for test_case in range(1,T+1):
    n, nums = input().split()
    n = int(n)

    is_delete = True
    while is_delete:
        is_delete = False
        for i in range(n-1):
            if nums[i] == nums[i+1]: # 이어진 두 수가 일치한다면
                nums = nums[:i] + nums[i+2:] # 인덱스 i와 i+1 부분을 제거
                n -= 2 #전체 길이 2 감소
                is_delete = True # while 문 탈출 조건 -> if 문에서 더 이상 줄이지 못했다면 탈출
                break # for문 탈출
    print(f'#{test_case} {nums}')