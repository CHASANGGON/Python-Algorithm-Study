T = int(input())

for tc in range(1,T+1):
    n = int(input())
    
    i = 1
    while n > i**3:
        i += 1
    
    if n == i**3:
        print(f'#{tc} {i}')
    else:
        print(f'#{tc} {-1}')