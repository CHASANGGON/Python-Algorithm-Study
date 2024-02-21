T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    lst = [list(map(int,input().split())) for _ in range(N)]
    lst_90 = []
    lst_180 = []
    lst_270 = []

    for i in range(N):
        for j in range(N):
            lst_90  += [lst[N-1-j][i]]      # 90
            lst_180 += [lst[N-1-i][N-1-j]]  # 180
            lst_270 += [lst[j][N-1-i]]      # 270

    # 편한 출력을 위해 lst_total에 옮겨담기
    lst_total = []
    for i in range(N):
            lst_total += lst_90[N*i:N*i+N]
            lst_total += lst_180[N*i:N*i+N]
            lst_total += lst_270[N*i:N*i+N]

    spacing = N         # N이 3일 경우, 3개 출력마다 띄어씀
    line_change = N*3   # N이 3일 경우, 9개 출력마다 줄바꿈

    print(f'#{test_case}')
    for i in range(3*N**2):
        if i // spacing and i % spacing == 0:
            print(' ',end='')
        if i // line_change and i % line_change == 0:
            print()
        print(lst_total[i],end='')
    print()