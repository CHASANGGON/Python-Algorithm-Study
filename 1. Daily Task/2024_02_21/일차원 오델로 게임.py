t = int(input())

for tc in range(1,t+1):
    n, m = map(int,input().split())
    stone = list(map(int,input().split()))
    
    for _ in range(m):
        i, j, o = map(int,input().split())
        i -= 1
    
        if o == 1:
            for idx in range(i,i+j):
                
                if idx < n and stone[idx] == 1:
                    stone[idx] = 0
                    
                elif idx < n and stone[idx] == 0:
                    stone[idx] = 1
                    
                    
        elif o == 2:
            c = stone[i]
            for idx in range(i+1,i+j):
                if idx < n: stone[idx] = c
                
        else:
            for idx in range(1,j+1):
                
                if i + idx < n and i - idx >= 0 and stone[i+idx] == stone[i-idx]:
                    
                    if stone[i+idx]:
                        stone[i+idx], stone[i-idx] = 0, 0
                    else:
                        stone[i+idx], stone[i-idx] = 1, 1
                    
    print(f'#{tc} ',end='')
    print(*stone)