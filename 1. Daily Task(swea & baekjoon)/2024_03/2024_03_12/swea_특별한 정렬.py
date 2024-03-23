# 선택 정렬
T = int(input())

for test_case in range(1,1+T):
    N = int(input())

    lst = list(map(int,input().split()))

    for i in range(N-1):
        target = i
        for j in range(i,N):
            # i가 짝수면 내림차순 정렬
            # 범위내에서 가장 큰 수를 찾기
            if i % 2 == 0:
                # 최댓값의 인덱스 갱신
                if lst[j] > lst[target]:
                    target = j
            # i가 홀수면 오름차순 정렬
            # 범위내에서 가장 작은 수를 찾기
            else:
                # 최솟값의 인덱스 갱신
                if lst[j] < lst[target]:
                    target = j
        # 값을 교환
        lst[i], lst[target] = lst[target], lst[i]
        
    print(f'#{test_case} ',end='')
    for i in range(10):
        print(lst[i], end=' ')
    print()