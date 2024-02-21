T = int(input())
for test_case in range(1,1+T):
    N, Q = map(int,input().split())
    boxes = [0]*N

    for i in range(1,Q+1):
        L, R = map(int,input().split())
        for j in range(L-1,R):
            boxes[j] = i

    print(f'#{test_case} ',end='')
    print(*boxes)