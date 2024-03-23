def h_to_b(h, i):
    j = 3
    while h:
        b[4*i+j] = h % 2
        j -= 1
        h //= 2

T = int(input())

chart = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

for tc in range(1,T+1):
    n, h = input().split()
    h = list(h)
    n = int(n)
    b = [0]*(4*n)
    for i in range(n):
        if h[i] in chart:
            h[i] = chart[h[i]]
        else:
            h[i] = int(h[i])

        h_to_b(h[i], i)
    
    print(f'#{tc} ',end='')
    for i in range(n*4):
        print(b[i],end='')
    print()