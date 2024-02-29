# 완탐 + 가지치기
# 딕셔너리?를 사용해서 같은 상태는 더 이상 탐색 x

# 완전탐색 (DFS)

t = int(input())

for tc in range(1,t+1):
    
    numbers, change = input().split() # target, baseline condition
    numbers = list(numbers) # for swap
    change = int(change) # ['1','2','3']
    
    # 숫자판의 갯수 N
    N = len(numbers)
    
    # (레벨, 숫자)의 중복을 제거하기 위한 변수
    history = set()
    # 로직
    # 완전 탐색 DFS
    mx = 0

    # 현재 교환 횟수를 K
    def dfs(k):
        global mx
        # 가지치기 : 같은 레벨에 같은 숫자 (레벨, 숫자)가 있다면 가지치기 하겠다...!        
        if (k, int(''.join(numbers))) in history:
            return 
        # 히스토리에 기록...! (레벨, 숫자)
        history.add((k, int(''.join(numbers))))
        # 기저 조건 : K 번 교환했다면 종료!
        if k == 0:
            # k번 교환한 번호판 <--- numbers 완성...!
            # 만들어진 numbers 번호판으로 최댓값을 갱신
            temp = int(''.join(numbers)) # 123
            mx = max(mx, temp)
            return

        # 재귀호출
        # 두 카드의 값을 교환... i번 째 카드와 j번 째를 교환
        for i in range(N - 1): # i : 0 -> N - 2
            for j in range(i + 1, N): # j : i + 1 -> N - 1
                # i <-> 교환 (결정)
                numbers[i], numbers[j] = numbers[j], numbers[i]
                dfs(k - 1)
                # i <-> 교환 (복구)
                numbers[i], numbers[j] = numbers[j], numbers[i]

    dfs(change)

    # 출력
    print(f'#{tc} {mx}')