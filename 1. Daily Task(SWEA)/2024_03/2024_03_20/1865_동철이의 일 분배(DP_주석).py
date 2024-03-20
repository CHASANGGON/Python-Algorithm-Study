# 동철이 DP!!!
import sys
sys.stdin = open('input.txt', 'r')

# N개의 일을 N명의 사원에게 일대일로 나눠줬을 때의 확률 최대값을 반환
def solve(N, P):
    
    # 메모리 공간 : 기존 중간 계산값을 저장 -> 활용!!
    
    # 피보나치 함수는 memo[n] 이렇게 쓰면 쉽게 재활용 가능..
    # But.. n명의 사원이 어떻게 일을 분배받았는지를 인덱스를 사용해 알기가 어렵다..
    
    # 메모이제이션(+비트마스크)에 현재까지 진행된 일들 - 현재까지의 일의 최대확률"을 매칭
    # memo[tuple(task)] = max(최대확률1, 최대확률2, ...) 
    
    memo = [0] * ((1 << N) - 1)
    
    # 최대 확률을 메모이제이션을 활용하여 계산을 수행하겠다..!
    def find_max_p(idx, task):
        # 기저 조건 : 모든 일을 다 수행하였을 때...!
        if task == (1 << N) - 1:
            return 100 # 확률을 100% 시작
        
        # 메모이제이션 : 재사용...
        if memo[task] != 0:
            return memo[task]
        
        # 재귀 호출
        # idx번째 사람 j번째 일을 할 때...!
        for j in range(N):
            # task 내에서 아직 j번쨰 일을 하지 않은 상황!
            if not task & (1 << j):
                # 비트 연산 : 작업할 j번쨰 일을 맡고, 다음 직원에게 일을 선택 진행!!
                new_p = P[idx][j] * find_max_p(idx + 1, task | (1 << j))
                # 임시 메모의 값을 최대 확률로 갱신!
                memo[task] = max(memo[task], new_p)
        
        # 최종적으로 계산된 최대 확률을 반환!!
        return memo[task]
                
    # idx 번째 사람까지 모든 일을 진행하였을 때의 계산값을 알아보자..!
    return find_max_p(0, 0)
    
    
    # # task 가 5개 인 상황
    # # task : 현재까지 진행한 일들의 번호를 체크해둔 배열
    # task = 0b00000 # 이진수...! [False] * N
    
    # # 2번쨰ㅣㅇㄹ과 3번쨰 일을 했다...!
    # task[1] = True
    # task[2] = True
    # task = 0b01100
    
    # # 모든 일을 다 했을 때...!
    # task = (1 << N) - 1
    
    
    
    return mx_p




# 테스트 케이스 수 T
T = int(input())

for tc in range(1, T + 1):
    # 입력
    # 일의 갯수 = 사원의 수 N
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    # 확률 (퍼센트 정수) -> 실수
    for i in range(N):
        for j in range(N):
            P[i][j] /= 100

    # 로직
    answer = solve(N, P)

    # 출력
    print(f"#{tc} {answer/100:.6f}")
    
    
    