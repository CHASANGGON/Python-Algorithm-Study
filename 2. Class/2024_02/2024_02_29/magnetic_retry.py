T = 10

for tc in range(1, T+1):
    n = int(input())

    arr = [list(map(int,input().split())) for _ in range(n)]

    cnt = 0
    stack = []
    for i in range(n):
        # 열이 바뀔 때 마다 stack 초기화
        stack = []
        for j in range(n):
            # 1은 아래로 끌리고
            # 2는 위로 끌린다
            if arr[j][i] == 1:
                stack.append(1)
            elif arr[j][i] == 2 and stack and stack[-1] == 1:
                cnt += 1
                stack = []
    
    print(f'#{tc} {cnt}')