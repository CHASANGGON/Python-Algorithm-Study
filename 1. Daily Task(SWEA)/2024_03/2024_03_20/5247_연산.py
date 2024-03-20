t = int(input())

for tc in range(1,t+1):
    n, m = map(int, input().split())
    
    # +1, -1, *2, -10
    
    cnt = 0
    
    while n*2 - m < m - n:
        n *= 2
        cnt += 1
    
    if n > 10:
        
    else:
        
    

    
    
    print(f'#{tc} {cnt}')