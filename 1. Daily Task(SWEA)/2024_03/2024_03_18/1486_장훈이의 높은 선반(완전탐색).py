t = int(input())
 
for tc in range(1,t+1):
    n, b = map(int,input().split())
    s_lst = list(map(int,input().split()))
     
    # 완전 탐색
    min_s = 99999999
     
    for i in range(1<<n):
        s = 0
        for j in range(n):
            if i & 1<<j:
                s += s_lst[j]
            if s >= b:
                min_s = min(min_s,s)
                break
             
    print(f'#{tc} {min_s-b}')