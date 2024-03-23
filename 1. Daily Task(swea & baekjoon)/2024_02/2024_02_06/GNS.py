T = int(input())

for test_case in range(1,T+1):
    input()
    nums = list(input().split())
    kind_of_nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # key값을 주고 빈 딕셔너리 생성
    dic = dict.fromkeys(kind_of_nums)
    
    # 딕셔너리의 value 초기화
    for k in dic.fromkeys(dic):
        dic[k] = 0

    # 딕셔너리의 key-value 카운팅
    for num in nums:
        dic[num] += 1

    # 출력
    print(f'#{test_case}')
    for k in dic.keys():
        while dic[k] > 0:
            print(k, end=' ')
            dic[k] -= 1
    print()