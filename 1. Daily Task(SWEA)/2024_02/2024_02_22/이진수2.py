def f(n):
    point = ''
    comp = []
    
    while n != 0:
        comp.append(n)
        
        if len(point) >= 13:
            print(f'#{tc} overflow')
            return
        
        n *= 2       
        if n >= 1.0:
            point += '1'
            n -= 1
        else:
            point += '0'
    
    print(f'#{tc} {point}')


import math
T = int(input())

for tc in range(1,T+1):
    n = float(input())
        
    f(n)