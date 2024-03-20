# N개의 일을 N명의 사원에게 일대일로 나눠줬을 때의 확률 최댓값을 반환!
def solve(N, P):
    # 임시 최댓값 변수 mx_p
    mx_p = 0
    # 방문체크를 할 배열
    worked = [False] * N
    
    # 백트래킹 : DFS + 가지치기
    # idx : 현재의 직원 번호
    # rate : 현재까지의 확률 값
    def find_max_p(idx, rate):
        # global은 아니고 local도 아닐 때 : enclosed
        nonlocal mx_p
        # 기저조건 (종료조건) : 모든 직원이 일을 진행하는 경우..
        if idx == N:
            mx_p = max(mx_p, rate)
            return
        # 가지치기 조건...!
        if rate <= mx_p:
            return
        # idx번째 사원이 0 ~ N-1 번째 일을 각각 해보는 경우를 보겠다...!
        for j in range(N): # j번째 일
            # P[idx][j] 성공확률
            # 다음 직원이 하도록 과정을 넘겨준다.
            if not worked[j]:
                worked[j] = True
                find_max_p(idx + 1, rate * P[idx][j])
                worked[j] = False    
        
    # 0번째 직원부터 일을 선택할 건데, 초기 확률을 100%로 주고 시작    
    find_max_p(0, 100)
    return mx_p

import sys
sys.stdin = open('C:/Users/SSAFY/Documents/GitHub/Algorithm/1. Daily Task(SWEA)/2024_03/2024_03_20/input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    # 입력
    # 일의 개수, 사원의 수 N
    N = int(input())
    # 확률 테이블 P
    P = [list(map(int, input().split())) for _ in range(N)]
    
    # 확률(퍼센트 정수) -> 실수
    for i in range(N):
        for j in range(N):
            P[i][j] /= 100
    
    # 로직
    answer = solve(N, P)    
    
    # 출력
    print(f'#{tc} {answer:.6f}')