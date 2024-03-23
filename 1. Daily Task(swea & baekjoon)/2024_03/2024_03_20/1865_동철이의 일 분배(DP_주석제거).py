def solution(P, N):
    memo = {}  # 딕셔너리로 메모이제이션
 
    # 현재까지 진행된 작업 내용
    def solve(idx, task):
        if all(task):  # task == [1] * N:  # 모든 작업이 배치된 경우
            return 100
        if tuple(task) in memo:  # 메모 활용
            return memo[tuple(task)]
 
        mx_p = 0
        for j in range(N):
            if task[j] == 0:
                task[j] = 1
                prob = P[idx][j] * solve(idx + 1, task)
                task[j] = 0
                mx_p = max(mx_p, prob)
 
        memo[tuple(task)] = mx_p
        return mx_p
 
    return solve(0, [0] * N)
 
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
 
    P = [list(map(int, input().split())) for _ in range(N)]
    for i in range(len(P)):
        for j in range(len(P[i])):
            P[i][j] /= 100
 
    print(f"#{tc} {solution(P, N):.6f}")