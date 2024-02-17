t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst_90 = []
    lst_180 = []
    lst_270 = []
    for i in range(n):
        for j in range(n):
            lst_90  += [lst[n-1-j][i]]      # 90
            lst_180 += [lst[n-1-i][n-1-j]]  # 180
            lst_270 += [lst[j][n-1-i]]      # 270
    n_lst_90 = [lst_90[i:i+n] for i in range(0, len(lst_90), n)]
    n_lst_180 = [lst_180[i:i+n] for i in range(0, len(lst_180), n)]
    n_lst_270 = [lst_270[i:i+n] for  i in range(0, len(lst_270), n)]
    
    print(f'#{tc}')
    for i in range(n):
        print(''.join(map(str, n_lst_90[i])), ''.join(map(str, n_lst_180[i])), ''.join(map(str, n_lst_270[i])))